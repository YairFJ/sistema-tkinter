from tkinter import *
from tkinter import ttk, messagebox
from modulos.utils import centrar_ventana, guardar, verificar_existencia_usuario
from modulos.articulos import moduloArticulos
from modulos.clientes import moduloClientes
from modulos.compras import moduloCompras
from modulos.configuracion import moduloConfiguracion
from modulos.ventas import moduloVentas
from modulos.proveedores import moduloProveedores
from modulos.estilos import misEstilos
from PIL import Image, ImageTk







colorNegro= "#000000"
colorNegro2= "#363636"
letraNegra= "#000000"
letraBlanca= "#FFFFFF" 
botonPresionado= "#D8FFF3"
botonActivo= "#6D97FF"
submenu = "#9AB7FF"


## LOGIN ##
def login():
    misEstilos(colorNegro, colorNegro2, colorNegro2, letraBlanca)
    centrar_ventana(ventana,600, 600)
    ventana.title("Login")
    ventana.resizable(False,False)
    
    def ingresar():
        frameLogin.pack_forget()
        principal()


    frameImagenLogin = ttk.Frame(ventana)
    frameImagenLogin.place(x=0,y=20)

    frameLogin = ttk.Frame(ventana, style="login.TFrame")
    frameLogin.pack(fill=BOTH, expand=1)


    imagen_pil = Image.open("images/WPHONE.png")
    imagen_pil = imagen_pil.resize((300,250), Image.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen_pil)
    labelImagen = ttk.Label(frameLogin, border=0)
    labelImagen.config(image=imagen_tk)
    labelImagen.image = imagen_tk   
    labelImagen.pack()



    
    frameDatosLogin = ttk.Frame(frameLogin, style="login.TFrame")
    frameDatosLogin.pack(fill=BOTH, pady=50)
    labelUsuario = ttk.Label(frameDatosLogin, text="Usuario",background="black", font=("Calibri",15), foreground="white")
    labelUsuario.pack(pady=10)
    entryUsuarioLogin = Entry(frameDatosLogin, width=40, bd=0,)
    entryUsuarioLogin.pack()

    labelContraseña = ttk.Label(frameDatosLogin, text="Contraseña",background="black", font=("Calibri",15), foreground="white")
    labelContraseña.pack(pady=10)
    entryContraseñaLogin = Entry(frameDatosLogin, width=40, bd=0, show="*")
    entryContraseñaLogin.pack()
    
    """img = PhotoImage(file='images/login.png')
    imagen = Label(frameLogin, image=img, border=0)
    imagen.pack()
"""
    """ frameImagenLogin = ttk.Frame(frameLogin, style="login.TFrame")
    frameImagenLogin.pack(fill=BOTH, expand=1) """
    frameBotonesLogin = ttk.Frame(frameLogin, style="login.TFrame")
    frameBotonesLogin.pack(fill=X)

    


    def log():
        usuario = entryUsuarioLogin.get()
        contraseña = entryContraseñaLogin.get()
        try:
            if (verificar_existencia_usuario(usuario,contraseña)):
                ingresar()
            else:
                messagebox.showerror("Login","El usuario o contraseña es incorrecto")

        except:
            messagebox.showwarning("Login","No existe ese usuario o contraseña")



    botonIngresar = ttk.Button(frameBotonesLogin, text="Ingresar", command=log, style="boton.TButton", cursor="hand2")
    botonIngresar.pack(pady=10, ipadx=40)
    frameRegistrarse = ttk.Frame(frameLogin)
    frameRegistrarse.pack()

    labelNoTienesCuenta = ttk.Label(frameRegistrarse, text="No tenés cuenta?",background="black", font=("Calibri",12), foreground="white")
    labelNoTienesCuenta.pack()

    frameRegistro = ttk.Frame(ventana, style="registro.TFrame")

    labelRegistrarse = ttk.Label(frameRegistro, text="Registro", style="titulosR.TLabel")
    
    frameDatosRegistro = ttk.Frame(frameRegistro, style="registro.TFrame")
    
    labelUsuario = ttk.Label(frameDatosRegistro, text="Usuario",style="subtitulosR.TLabel")
    labelUsuario.pack(pady=10)
    entryUsuarioRegistro = Entry(frameDatosRegistro, width=40, bd=0,)
    entryUsuarioRegistro.pack()
  
    labelContraseña = ttk.Label(frameDatosRegistro, text="Contraseña",style="subtitulosR.TLabel")
    labelContraseña.pack(pady=10)
    entryContraseñaRegistro = Entry(frameDatosRegistro, width=40, bd=0, show="*")
    entryContraseñaRegistro.pack()

    
    frameBotonesRegistro = ttk.Frame(frameRegistro, style="registro.TFrame")

    def registrarse():
        datos = (entryUsuarioRegistro.get(), entryContraseñaRegistro.get(),)

        if ( entryUsuarioRegistro.get() != "" and entryContraseñaRegistro.get != ""):


            try:
                guardar(datos)
                entryUsuarioRegistro.delete(0, END)
                entryContraseñaRegistro.delete(0, END)
                messagebox.showinfo("Registro","Te has registrado correctamente")

            
            
            except BaseException as err:
                print(err)
                messagebox.showerror("Registro","Ha ocurrido un error")

        else:
            messagebox.showinfo("Registro","No puede ingresar datos vacios")


    botonRegistrarse = ttk.Button(frameBotonesRegistro, text="Registrarse", command=registrarse, style="boton.TButton", cursor="hand2")
    botonRegistrarse.pack(pady=40, ipadx=40)

    
    frameInfoRegistro = ttk.Frame(ventana, style="registro.TFrame")

    labelTenesCuenta = ttk.Label(frameInfoRegistro, text="Ya tenés cuenta?", background="#9AB7FF", font=("Calibri",12), foreground="black")
    

    def registro():
        frameLogin.pack_forget()
        frameRegistro.pack(fill=BOTH, expand=1)
        frameInfoRegistro.pack(fill=BOTH)
        labelRegistrarse.pack(pady=30)
        frameDatosRegistro.pack(fill=BOTH, pady=50)
        frameBotonesRegistro.pack(fill=X)
        labelTenesCuenta.pack()
        botonIngresar.pack()
        

    def loguearse():
        frameLogin.pack(fill=BOTH, expand=1)
        frameRegistro.pack_forget()
        frameInfoRegistro.pack_forget()
        labelRegistrarse.pack_forget()
        frameDatosRegistro.pack_forget()
        frameBotonesRegistro.pack_forget()
        labelTenesCuenta.pack_forget()
        botonIngresar.pack_forget()


    botonIngresar = Button(frameInfoRegistro, text="Ingresa",background="#9AB7FF", font=("Calibri",13), foreground="red",bd=0, cursor="hand2", command=loguearse)
        
    
    botonRegistrate = Button(frameRegistrarse, text="Registrate",background="black", font=("Calibri",13), foreground="blue",bd=0, cursor="hand2", command=registro)
    botonRegistrate.pack(fill=BOTH)

    
############

## PRINCIPAL ##
def principal():
    centrar_ventana(ventana,1280,950)
    ventana.title("Principal")
    moduloNavegacion(ventana)

#############################################################################

def moduloNavegacion(ventana):
    frameBotones = ttk.Frame(ventana,style="botones.TFrame")
    
    frameBotones.pack(side=TOP ,fill=X)

    frameContenido = ttk.Frame(ventana,style="contenido.TFrame")
    frameContenido.pack(fill=BOTH, expand=1) # expand1

    frameClientes = ttk.Frame(frameContenido, style="clientes.TFrame")

    frameProveedores = ttk.Frame(frameContenido, style="contenido.TFrame")

    frameArticulos = ttk.Frame(frameContenido, style="contenido.TFrame")

    frameCompras = ttk.Frame(frameContenido, style="contenido.TFrame")

    frameVentas = ttk.Frame(frameContenido, style="contenido.TFrame")

    frameConfiguracion = ttk.Frame(frameContenido, style="contenido.TFrame")

    def sacarFrames():
        frameClientes.pack_forget()
        frameProveedores.pack_forget()
        frameArticulos.pack_forget()
        frameCompras.pack_forget()
        frameVentas.pack_forget()
        frameConfiguracion.pack_forget()

    
    def resetColorBotones():
        botonClientes.config(style="boton.TButton")
        botonProveedores.config(style="boton.TButton")
        botonArticulos.config(style="boton.TButton")
        botonVentas.config(style="boton.TButton")
        botonCompras.config(style="boton.TButton")
        botonConfiguracion.config(style="boton.TButton")

    def checkModules(modulo):
        if(modulo in globals()):
            return True
        return False

    def clientes():
        sacarFrames()
        frameClientes.pack(fill=BOTH, expand=1)
        resetColorBotones()
        botonClientes.config(style="botonPresionado.TButton")
        if(not(checkModules('cli'))):
            global cli
            cli = moduloClientes(frameClientes)

    botonClientes = ttk.Button(frameBotones, text="Clientes", command=clientes, style="boton.TButton")
    botonClientes.pack(side=LEFT, ipady=10, expand=1,fill=BOTH)

    

    def proveedores():
        sacarFrames()
        frameProveedores.pack(fill=BOTH, expand=1)
        resetColorBotones()
        botonProveedores.config(style="botonPresionado.TButton")
        if(not(checkModules('prov'))):
            global prov
            prov = moduloProveedores(frameProveedores)

    botonProveedores = ttk.Button(frameBotones, text="Proveedores", command=proveedores, style="boton.TButton")
    botonProveedores.pack(side=LEFT, ipady=10, expand=1,fill=BOTH)

    ## ARTICULOS ##
    
    def articulos():
        sacarFrames()
        frameArticulos.pack(fill=BOTH,expand=1)
        resetColorBotones()
        botonArticulos.config(style="botonPresionado.TButton")
        if(not(checkModules('art'))):
            global art
            art = moduloArticulos(frameArticulos)
        
    botonArticulos = ttk.Button(frameBotones, text="Articulos", command=articulos, style="boton.TButton")
    botonArticulos.pack(side=LEFT, ipady=10, expand=1,fill=BOTH)
    ######################################################################

    def compras():
        sacarFrames()
        frameCompras.pack(fill=BOTH, expand=1)
        resetColorBotones()
        botonCompras.config(style="botonPresionado.TButton")
        if(not(checkModules('com'))):
            global com
            com = moduloCompras(frameCompras)

    botonCompras = ttk.Button(frameBotones, text="Compras", command=compras, style="boton.TButton")
    botonCompras.pack(side=LEFT, ipady=10, expand=1,fill=BOTH)


    def ventas():
        sacarFrames()
        resetColorBotones()
        frameVentas.pack(fill=BOTH, expand=1) 
        botonVentas.config(style="botonPresionado.TButton")
        if(not(checkModules('vent'))):
            global vent
            vent = moduloVentas(frameVentas)

    botonVentas = ttk.Button(frameBotones, text="Ventas", command=ventas, style="boton.TButton")
    botonVentas.pack(side=LEFT, ipady=10, expand=1,fill=BOTH)  
    
    ## CONFIGURACION ##
    def configuracion():
        sacarFrames()
        frameConfiguracion.pack(fill=BOTH, expand=1)
        resetColorBotones()
        botonConfiguracion.config(style="botonPresionado.TButton")
        if(not(checkModules('conf'))):
            global conf
            conf = moduloConfiguracion(frameConfiguracion)

    botonConfiguracion = ttk.Button(frameBotones, text="⚙️Configuracion", command=configuracion, style="boton.TButton")
    botonConfiguracion.pack(side=RIGHT, ipady=10, expand=1,fill=BOTH)
    


if __name__ == "__main__":
    global ventana
    ventana = Tk()
    ventana.geometry("600x600")
    login()
    ventana.mainloop()
