from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from modulos.utils import limpiar_treeview, conectar, today
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime


global carrito
carrito = []


def moduloVentas(frameVentas):

    fecha = today()

    frameContenidoVenta = ttk.Frame(frameVentas, style="contenido.TFrame")
    frameTablaVenta = ttk.Frame(frameContenidoVenta,style="contenido.TFrame")
    frameBotonesVenta = ttk.Frame(frameContenidoVenta,style="submenu.TFrame")
    frameBotonesVenta.pack(side=LEFT, fill=BOTH)
    frameContenidoVenta.pack(side=LEFT,fill=BOTH, expand=1)
    frameTablaVenta.pack()
    frameFecha = ttk.Frame(frameTablaVenta, style="contenido.TFrame")
    frameFecha.pack(pady=30)
 ########################################################
    def resetColorBotonesSubmenu():
        botonVenderArticulo.config(style="btsubmenu.TButton")
        botonAgregarArticulo.config(style="btsubmenu.TButton")

    def vaciarEntrys():
        entrySubTotalVenta.delete(0, END)
        entryIvaVenta.delete(0, END)
        entryTotalVenta.delete(0, END)

    
   
    ################### TABLA VENTAS ####################
    labelFechaVenta = ttk.Label(frameFecha,text="Fecha Venta",style="entrada.TLabel")
    entryFechaVenta = ttk.Entry(frameFecha, font=("Calibri,14"))
    labelFechaVenta.pack(anchor=N)
    entryFechaVenta.pack(anchor=N)

    
    entryFechaVenta.insert("0",fecha)
    entryFechaVenta.config(state='readonly')

    tablaVenta = ttk.Treeview(frameTablaVenta,style="tablaBuscar.Treeview")
    tablaVenta["columns"] = ("cantidad","subtotal")

    tablaVenta.heading("#0",text="Detalles")
    tablaVenta.heading("cantidad",text="Cantidad")
    tablaVenta.heading("subtotal",text="Subtotal")
    

    tablaVenta.pack(pady=30,padx=80,fill=BOTH,ipadx=100,ipady=100)
    #####################################################

    def agregarArticulo():
        resetColorBotonesSubmenu()
        global ventanaAgregarArticulo
        if('ventanaAgregarArticulo' in globals()):
            ventanaAgregarArticulo.destroy()
        ventanaAgregarArticulo = Toplevel(bg="#000000")

        botonAgregarArticulo.config(style="botonPresionado.TButton")

        labelBuscadorArticulosVenta = ttk.Label(ventanaAgregarArticulo,text="Búsqueda de articulos",style="entrada.TLabel")
        labelBuscadorArticulosVenta.pack(fill=X,padx=80,pady=(20,0),anchor=N)
        buscadorArticulosVenta = ttk.Entry(ventanaAgregarArticulo,font=("Calibri",14))
        buscadorArticulosVenta.pack(fill=X,padx=80,pady=(0,20))

        tablaArticulosVenta = ttk.Treeview(ventanaAgregarArticulo,style="tablaBuscar.Treeview")
        tablaArticulosVenta["columns"] = ("marca","modelo", "stock")
        tablaArticulosVenta.column("#0", minwidth=0,width=100,stretch=False , anchor=CENTER)
        
        tablaArticulosVenta.tag_configure("odd", background="#D8D7D7")
        tablaArticulosVenta.tag_configure("even", background="snow")

        tablaArticulosVenta.heading("#0",text="Código")
        tablaArticulosVenta.heading("marca",text="Marca")
        tablaArticulosVenta.heading("modelo",text="Modelo")
        tablaArticulosVenta.heading("stock",text="Stock")

        tablaArticulosVenta.pack(pady=10,padx=80,fill=BOTH,ipady=100)

        labelCantidadArticulosVenta = ttk.Label(ventanaAgregarArticulo,text="Cantidad",style="entrada.TLabel")
        labelCantidadArticulosVenta.pack()
        entryCantidadArticulosVenta = ttk.Entry(ventanaAgregarArticulo,font=("Calibri",14))
        entryCantidadArticulosVenta.pack(pady=10)
        #################################################

        

  

        def agregarArticulo(articulo):
            global carrito
            carrito.append(articulo)


        def verDatosTablaArticulosVenta(evt):
            if(entryCantidadArticulosVenta.get() == ""):
                messagebox.showwarning("Articulo","Ingrese una cantidad")
                return

            subTotalVenta = 0
            idFila = tablaArticulosVenta.selection()
            codigo = (tablaArticulosVenta.item(idFila)["text"],)
            conexion = conectar()
            tabla = conexion.cursor()
            tabla.execute("SELECT * FROM Articulos WHERE codigo=?", codigo)
            conexion.commit()

            ### CARRITO ###

            articuloBuscado = tabla.fetchall()
            precioCosto = articuloBuscado[0][4]
            ganancia = articuloBuscado[0][5]
            cantidad = int(entryCantidadArticulosVenta.get())
            subtotal = (precioCosto + (precioCosto*ganancia/100)) * cantidad
            iva = subtotal * 0.21
            total = subtotal + iva
            global stock
            stock = articuloBuscado[0][6]
            

            if (stock < 1):
                messagebox.showerror("Venta", "No hay stock")
                return

            if (stock < int(entryCantidadArticulosVenta.get())):
                messagebox.showerror("Venta","No contamos con el suficiente stock para esta venta.")
                return
            
            if(stock < 5):
                messagebox.showwarning("Venta", "Se está agotando el stock\n Contacte a su proveedor porfavor.")

            articuloVender = (articuloBuscado[0][0],
                              articuloBuscado[0][1] + " - " +articuloBuscado[0][2],
                              cantidad,
                              subtotal,
                              iva,
                              total)

            agregarArticulo(articuloVender)
            tablaVenta.insert("",END, text= articuloVender[1], values=(articuloVender[2],articuloVender[3],))
            for articulo in carrito:
                subTotalVenta += float(articulo[3])
            ivaVenta = subTotalVenta * 0.21
            totalVenta = subTotalVenta + ivaVenta
            entrySubTotalVenta.delete(0, END)
            entrySubTotalVenta.insert(END, subTotalVenta)
            entryIvaVenta.delete(0, END)
            entryIvaVenta.insert(END, ivaVenta)
            entryTotalVenta.delete(0, END)
            entryTotalVenta.insert(END, totalVenta)
            
        tablaArticulosVenta.bind("<<TreeviewSelect>>", verDatosTablaArticulosVenta)
        
        def buscador(dato):
            conexion = conectar()
            tabla = conexion.cursor()
            query = "SELECT * FROM Articulos WHERE marca LIKE ? OR modelo LIKE ?"
            tabla.execute(query, dato)
            conexion.commit() 
            for fila in tablaArticulosVenta.get_children():
                tablaArticulosVenta.delete(fila)
            for row in tabla:
                tablaArticulosVenta.insert("",END, text=row[0], values=(row[1],row[2],row[6]))
            tabla.close()


        def buscarArticulosVenta(evt):
            buscar = ("%"+buscadorArticulosVenta.get()+"%", "%"+buscadorArticulosVenta.get()+"%",)
            buscador(buscar)
            
        buscadorArticulosVenta.bind("<Key>",buscarArticulosVenta)
        buscarArticulosVenta("evt")

    def borrarItemVenta():
		#Borrar primero en el carrito(la lista)
            posicion = tablaVenta.index(tablaVenta.selection())
            carrito.pop(posicion)

		#Borrar la tabla visual(tablaVenta)
            fila = tablaVenta.selection()
            tablaVenta.delete(fila)
            subTotalVenta = 0
            for articulo in carrito:
                subTotalVenta = subTotalVenta + float(articulo[3]) 
            ivaVenta = subTotalVenta * 0.21
            totalVenta = subTotalVenta + ivaVenta
            entrySubTotalVenta.delete(0,END)
            entrySubTotalVenta.insert(END,subTotalVenta)
            entryIvaVenta.delete(0,END)
            entryIvaVenta.insert(END,ivaVenta)
            entryTotalVenta.delete(0,END)
            entryTotalVenta.insert(END,totalVenta)
    

    botonBorrarItem = ttk.Button(frameTablaVenta,text="Borrar Item",command=borrarItemVenta, style="boton.TButton")
    botonBorrarItem.pack()

    labelSubTotalVenta = ttk.Label(frameTablaVenta, text="Subtotal Venta", style="subtitulos.TLabel")
    labelSubTotalVenta.pack(fill=X,padx=80,pady=(20,0) ,anchor=W)
    entrySubTotalVenta = ttk.Entry(frameTablaVenta, font=("Calibri,14"))
    entrySubTotalVenta.pack(padx=80,anchor=W)

    labelIvaVenta = ttk.Label(frameTablaVenta, text="Iva Venta", style="subtitulos.TLabel")
    labelIvaVenta.pack(fill=X,padx=80,pady=(20,0) ,anchor=W)
    entryIvaVenta = ttk.Entry(frameTablaVenta, font=("Calibri,14"))
    entryIvaVenta.pack(padx=80,anchor=W)

    labelTotalVenta = ttk.Label(frameTablaVenta, text="Total Venta", style="subtitulos.TLabel")
    labelTotalVenta.pack(fill=X,padx=80,pady=(20,0) ,anchor=W)
    entryTotalVenta = ttk.Entry(frameTablaVenta, font=("Calibri,14"))
    entryTotalVenta.pack(padx=80,anchor=W)

    botonAgregarArticulo = ttk.Button(frameBotonesVenta, text="Agregar Articulo", style="boton.TButton", command=agregarArticulo)    
    botonAgregarArticulo.pack(ipadx=50, ipady=40,fill=X)

    

    def vender():
        global carrito
        resetColorBotonesSubmenu()
        botonVenderArticulo.config(style="botonPresionado.TButton")

        
        if(len(carrito) == 0):
            messagebox.showwarning("Venta", "No hay nada en el carrito")
            return


        try:
        
            ticket = imprimirTicket(entryIvaVenta.get(),entrySubTotalVenta.get(),entryTotalVenta.get())

            datosVenta = (entryFechaVenta.get(),entrySubTotalVenta.get(), entryIvaVenta.get(), entryTotalVenta.get(), ticket)

            conexion = conectar()
            tabla = conexion.cursor()

            for articulo in carrito:
                buscarCodigo = (articulo[0],)
                tabla.execute("SELECT stock FROM Articulos WHERE codigo=?", buscarCodigo)
                conexion.commit()
                buscarStock = tabla.fetchall()
                nuevaCantidad = buscarStock[0][0] - articulo[2]
                datos = (nuevaCantidad, articulo[0])
                tabla.execute("UPDATE Articulos SET stock=? WHERE codigo=?", datos)
                conexion.commit()
                


            tabla.execute("INSERT INTO Ventas(fechaVenta, subTotal, iva, total, ticket) VALUES (?,?,?,?,?)", datosVenta)
            conexion.commit()
            messagebox.showinfo("Venta", "Se ha realizado la venta correctamente")
            vaciarEntrys()
            limpiar_treeview(tablaVenta)

        
            tabla = conexion.cursor()
            tabla.execute("SELECT MAX(idVenta) FROM Ventas")
            datosBuscadosMaxIdVenta = tabla.fetchall()
            ultimoIdVenta = datosBuscadosMaxIdVenta[0][0]
            for articulo in carrito:
                datosArticulosVendidos = (ultimoIdVenta, articulo[0],articulo[2],articulo[5])
                tabla.execute("INSERT INTO articulosVendidos(idVenta, articuloVendido, cantidadVendida, totalVendido) VALUES(?,?,?,?)", datosArticulosVendidos)
                conexion.commit()
                
            carrito.clear()
            tabla.close()
    

        except BaseException as err:
            print(err)
            messagebox.showerror("Venta", "Ha ocurrido un error en la venta")
            vaciarEntrys()
            carrito.clear()
            


    botonVenderArticulo = ttk.Button(frameBotonesVenta, text="Vender Articulo ", style="boton.TButton", command=vender)
    botonVenderArticulo.pack(ipadx=50, ipady=40,fill=X)

    
    def imprimirTicket(iva,subtotal,total):
        fecha = datetime.now()
        horaActual = fecha.strftime('%d%m%Y%H%M%S')
        archivo = f"Tickets/ticket{horaActual}.pdf"
        pdf = canvas.Canvas(archivo,pagesize=A4)
        pdf.line(50,800,550,800)
        pdf.line(50,50,550,50)
        pdf.line(50,800,50,50)
        pdf.line(550,800,550,50)

        pdf.setFont("Times-Roman",30)
        pdf.drawString(250,750,"VENTAS")
        pdf.setFont("Times-Roman",15)
        y = 700
        for articulo in carrito:
            pdf.drawString(80,y,articulo[1])
            pdf.drawString(490,y,"$"+str(articulo[3]))
            y-=30
        pdf.drawString(400,200,"IVA")
        pdf.drawString(490,200,"$"+iva)
        pdf.drawString(400,150,"SUBTOTAL")
        pdf.drawString(490,150,"$"+subtotal)
        pdf.drawString(400,100,"TOTAL")
        pdf.drawString(490,100,"$"+total)
        pdf.save()
        return archivo