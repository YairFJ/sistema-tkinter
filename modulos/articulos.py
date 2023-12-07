from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from modulos.utils import conectar

def moduloArticulos(frameArticulos):
    frameContenidoArticulos = ttk.Frame(frameArticulos,style="contenido.TFrame")
    frameBotonesArticulos = ttk.Frame(frameArticulos,style="submenu.TFrame")
    frameBotonesArticulos.pack(side=LEFT, fill=BOTH)
    frameContenidoArticulos.pack(side=LEFT,fill=BOTH,expand=1)

    def resetColorBotonesSubmenu():
        botonBuscarArticulo.config(style="btsubmenu.TButton")
        botonNuevoArticulo.config(style="btsubmenu.TButton")
       
    def sacarFrameArticulos():
        frameBuscarArticulos.pack_forget()
        frameNuevoArticulo.pack_forget()

    def verBuscarArticulo():
        sacarFrameArticulos()
        frameBuscarArticulos.pack(fill=BOTH, expand=1)
        resetColorBotonesSubmenu()
        vaciarEntrys()
        botonBuscarArticulo.config(style="botonPresionado.TButton")
    botonBuscarArticulo= ttk.Button(frameBotonesArticulos,style="btsubmenu.TButton" ,text="Buscar Artículo", command=verBuscarArticulo)
    botonBuscarArticulo.pack(ipadx=50,ipady=40,fill=X)

    def verNuevoArticulo():
        sacarFrameArticulos()
        frameNuevoArticulo.pack(fill=BOTH, side=LEFT, padx=200,expand=1)
        resetColorBotonesSubmenu()
        vaciarEntrys()
        botonNuevoArticulo.config(style="botonPresionado.TButton")
        botonModificarArticulo.pack_forget()
        botonEliminarArticulo.pack_forget()
        botonGuardarArticulo.pack(pady= 100, anchor=S, ipadx=20)

    botonNuevoArticulo = ttk.Button(frameBotonesArticulos,style="btsubmenu.TButton", text="Nuevo Articulo", command=verNuevoArticulo)
    botonNuevoArticulo.pack(ipadx=50, ipady=40,fill=X)

    def verModificarArticulo():
        sacarFrameArticulos()
        vaciarEntrys()
        frameNuevoArticulo.pack(fill=BOTH, side=LEFT, padx=200,expand=1)
        botonGuardarArticulo.pack_forget()
        botonModificarArticulo.pack(pady= 100, side=LEFT, ipadx=20, padx=20)
        botonEliminarArticulo.pack(pady= 100, side=LEFT, ipadx=20, padx=20)

    frameBuscarArticulos = ttk.Frame(frameContenidoArticulos,style="contenido.TFrame")
    frameNuevoArticulo = ttk.Frame(frameContenidoArticulos,style="contenido.TFrame")

    

    def vaciarEntrys():
        entryIdArticulo.delete(0, END)
        entryMarca.delete(0, END)
        entryModelo.delete(0, END)
        entryDetalles.delete("1.0", END)
        entryPrecioCosto.delete(0, END)
        entryGanancia.delete(0, END)
        
        
    
    labelBuscadorArticulos = ttk.Label(frameBuscarArticulos,text="Búsqueda de articulos",style="entrada.TLabel")
    labelBuscadorArticulos.pack(fill=X,padx=80,pady=(20,0),anchor=N)
    buscadorArticulos = ttk.Entry(frameBuscarArticulos,font=("Calibri",14))
    buscadorArticulos.pack(fill=X,padx=80,pady=(0,20))
        
	
        ## Tabla Articulos ##
    tablaArticulos = ttk.Treeview(frameBuscarArticulos,style="tablaBuscar.Treeview")
    tablaArticulos["columns"] = ("marca","modelo","detalles","precio_costo", "ganancia")
    tablaArticulos.column("#0", minwidth=0,width=100,stretch=False , anchor=CENTER)
	
    tablaArticulos.tag_configure("odd", background="#D8D7D7")
    tablaArticulos.tag_configure("even", background="snow")

    tablaArticulos.heading("#0",text="Código")
    tablaArticulos.heading("marca",text="Marca")
    tablaArticulos.heading("modelo",text="Modelo")
    tablaArticulos.heading("detalles",text="Detalles")
    tablaArticulos.heading("precio_costo",text="Precio Costo")
    tablaArticulos.heading("ganancia",text="Ganancia")

    tablaArticulos.pack(pady=10,padx=80,fill=BOTH,ipady=100)

    def verDatosTablaArticulos(evt):
        idFila = tablaArticulos.selection()
        codigo = tablaArticulos.item(idFila)["text"]

        def buscar(dato):
            if(dato[0] != codigo):
                return False
            return True
        try:
            articulos = filter(buscar, datosBuscados)
            articulo = list(articulos)
            verModificarArticulo()
            entryIdArticulo.insert(0, articulo[0][0])
            entryMarca.insert(0,articulo[0][1])
            entryModelo.insert(0,articulo[0][2])
            entryDetalles.insert(1.0,articulo[0][3])
            entryPrecioCosto.insert(0,articulo[0][4])
            entryGanancia.insert(0,articulo[0][5])
        except IndexError as err:
            print(err)

    tablaArticulos.bind("<<TreeviewSelect>>", verDatosTablaArticulos)
    
    def busqueda(datos):
        global tabla
        conexion = conectar()
        tabla = conexion.cursor()
        query = "SELECT * FROM Articulos WHERE marca LIKE ? OR modelo LIKE ?"
        tabla.execute(query, datos)
        conexion.commit()
        global datosBuscados
        datosBuscados = tabla.fetchall()
        
        for fila in tablaArticulos.get_children():
            tablaArticulos.delete(fila)


        for dato in datosBuscados:
            tag = "even"
            if(datosBuscados.index(dato) % 2 != 0):
                tag = "odd"
            tablaArticulos.insert("",END,text=dato[0],values=(dato[1],dato[2], dato[3],dato[4],dato[5]), tags=(tag,))
        tabla.close()
      

    def buscarArticulos(evt):

        buscar = ("%"+buscadorArticulos.get()+"%", "%"+buscadorArticulos.get()+"%",)
        busqueda(buscar)


       
    buscadorArticulos.bind("<Key>",buscarArticulos)
    buscarArticulos("evt")
    entryIdArticulo =  ttk.Entry(frameNuevoArticulo)
    

    ################### Labels y Entrys Nuevo Articulo ######################
    
    labelMarca = ttk.Label(frameNuevoArticulo, text="Marca", style="subtitulos.TLabel")
    labelMarca.pack(pady=20, anchor=W)
    entryMarca = ttk.Entry(frameNuevoArticulo)
    entryMarca.pack(ipadx=60, ipady=3, anchor=W)
    labelModelo = ttk.Label(frameNuevoArticulo, text="Modelo", style="subtitulos.TLabel")
    labelModelo.pack(pady=20, anchor=W)
    entryModelo = ttk.Entry(frameNuevoArticulo)
    entryModelo.pack(ipadx=60, ipady=3, anchor=W)
    labelDetalles = ttk.Label(frameNuevoArticulo, text="Detalles", style="subtitulos.TLabel")
    labelDetalles.pack(pady=20, anchor=W)
    entryDetalles = Text(frameNuevoArticulo, width=50, height = 10)
    entryDetalles.pack(anchor=W)
    labelPrecioCosto = ttk.Label(frameNuevoArticulo, text="Precio Costo", style="subtitulos.TLabel")
    labelPrecioCosto.pack(pady=20, anchor=W)
    entryPrecioCosto = ttk.Entry(frameNuevoArticulo)
    entryPrecioCosto.pack(ipadx=60, ipady=3, anchor=W)
    labelGanancia = ttk.Label(frameNuevoArticulo, text="Ganancia", style="subtitulos.TLabel")
    labelGanancia.pack(pady=20, anchor=W)
    entryGanancia = ttk.Entry(frameNuevoArticulo)
    entryGanancia.pack(ipadx=60, ipady=3, anchor=W)
    #########################################################################
    def guardar(datos):
        global tabla
        conexion = conectar()
        tabla = conexion.cursor()
        query = "INSERT INTO Articulos (marca, modelo,detalles, precio_costo, ganancia, stock) VALUES (?,?,?,?,?,99)"
        tabla.execute(query, datos)
        conexion.commit()
        messagebox.showinfo("Articulos", "Se ha guardado correctamente el articulo")
        vaciarEntrys()
        tabla.close()

    def guardarArticulo():

        if entryMarca.get() != "" and entryModelo.get() != "" and entryDetalles.get("1.0", END) != "" and entryPrecioCosto.get() != "" and entryGanancia.get() != "":

            datos = (entryMarca.get(), entryModelo.get(),entryDetalles.get("1.0", END),entryPrecioCosto.get(), entryGanancia.get())

            try:
                guardar(datos)
                
            except BaseException as err:
                print(err)
                messagebox.showerror("Error01","Ha ocurrido un error")
                vaciarEntrys()
                
        else:
            messagebox.showerror("Error02", "Los campos que quiere guardar estan vacios")
            tabla.close()
        


    botonGuardarArticulo = ttk.Button(frameNuevoArticulo, text="Guardar Articulo", command=guardarArticulo, style="boton.TButton")
    
    def modificar(datos):
        conexion = conectar()
        tabla = conexion.cursor()
        query = "UPDATE Articulos SET marca = ?, modelo =?,detalles=?, precio_costo=?, ganancia=? WHERE codigo = ?"
        tabla.execute(query,datos)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Articulos", "Se ha modificado correctamente el articulo")
        vaciarEntrys()
        verBuscarArticulo()

    def modificarArticulo():

        if entryMarca.get() != "" and entryModelo.get() != "" and entryDetalles.get("1.0", END) != "" and entryPrecioCosto.get() != "" and entryGanancia.get() != "" and entryIdArticulo.get() != "":

            datos = (entryMarca.get(), entryModelo.get(),entryDetalles.get("1.0", END),entryPrecioCosto.get(), entryGanancia.get(), entryIdArticulo.get())
        
            try:
                
               modificar(datos)
                
            except:
                messagebox.showerror("Error01","Ha ocurrido un error")
                vaciarEntrys()
                
        else:
            messagebox.showerror("Error02", "Los campos que quiere modificar están vacios")
            tabla.close()
            
        

    botonModificarArticulo = ttk.Button(frameNuevoArticulo, text="Modificar Articulo", command=modificarArticulo, style="boton.TButton")

    verBuscarArticulo()

    def eliminar(codigo):
        conexion = conectar()
        tabla = conexion.cursor()
        query = "DELETE FROM Articulos WHERE codigo = ? "
        tabla.execute(query,codigo)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Articulos", "Se ha eliminado correctamente el articulo")
        vaciarEntrys()
        verBuscarArticulo()
        

    def eliminarArticulo():

        if entryIdArticulo.get() != "":

            codigo = (entryIdArticulo.get(),)
        
            try:
                
                eliminar(codigo)
               
                
            except:
                messagebox.showerror("Error01","Ha ocurrido un error")
                vaciarEntrys()
                
        else:
            messagebox.showerror("Error02", "Los campos que quiere modificar están vacios")
            tabla.close()
            
        

    botonEliminarArticulo = ttk.Button(frameNuevoArticulo, text="Eliminar Articulo", command=eliminarArticulo, style="boton.TButton")

    