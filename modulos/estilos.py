from tkinter import *
from tkinter import ttk

colorNegro= "#000000"
colorNegro2= "#363636"
letraNegra= "#000000"
letraBlanca= "#FFFFFF" 
botonPresionado= "#D8FFF3"
botonActivo= "#6D97FF"
submenu = "#9AB7FF"



def misEstilos(colorFondo, colorFondo2, colorBoton, colorLetra):
    estilos = ttk.Style()
    estilos.theme_use("alt")
    
    estilos.configure("login.TFrame",
                      background= colorFondo
    )

    estilos.configure("registro.TFrame",
                      background= submenu
    )

    estilos.configure("botones.TFrame",
                      background= colorFondo
    )

    estilos.configure("contenido.TFrame",
                      background= "colorFondo"
    )

    estilos.configure("contenido2.TFrame",
                      background= "red"
    )

    estilos.configure("contenido3.TFrame",
                      background= "blue"
    )

    estilos.configure("submenu.TFrame",
                      background = submenu
    )

    estilos.configure("clientes.TFrame",
                      background= colorFondo
    )

    estilos.configure("entry.TEntry",
                      background= colorLetra,
                      padding=20
    )

    estilos.configure("btsubmenu.TButton",
                      background= botonActivo,
                      foreground = colorLetra,
                      font=("Calibri", 15),
                      relief=FLAT
    )

    estilos.configure("boton.TButton",
                      background = colorBoton,
                      foreground = colorLetra,
                      font=("Calibri", 15),
                      relief=FLAT
                )
    
    estilos.configure("botonPresionado.TButton",
                      background = colorFondo2,
                      foreground = colorLetra,
                      font=("Calibri", 15),
                      relief=FLAT
                )

    estilos.map("boton.TButton",
                    background = [("pressed", colorBoton),("active", colorBoton)]
                )

    estilos.map("btsubmenu.TButton",
                    background = [("pressed", colorNegro),("active", colorNegro)]
                )

    estilos.configure("titulos.TLabel",
                       background=colorFondo,
                       font=("Calibri", 20),
                       foreground= colorLetra,
                       relief= FLAT
    )

    estilos.configure("titulosR.TLabel",
                       background=submenu,
                       font=("Calibri", 20),
                       foreground= colorNegro,
                       relief= FLAT
    )

    estilos.configure("subtitulos.TLabel",
                       background=colorFondo,
                       font=("Calibri", 15),
                       foreground= colorLetra,
                       relief= FLAT
    )

    estilos.configure("subtitulosR.TLabel",
                       background=submenu,
                       font=("Calibri", 15),
                       foreground= colorNegro,
                       relief= FLAT,
                       bd=0,

    )

    estilos.configure("subtitulo.TLabel",
                       background="red",
                       font=("Calibri", 15),
                       foreground= "white",
                       relief= FLAT
    )

    estilos.configure("entrada.TLabel",
                       background=colorFondo,
                       font=("Calibri", 15),
                       foreground= colorLetra,
                       relief= FLAT
    )

    estilos.configure("tablaBuscar.Treeview", 
					   highlightthickness=0,
					   bd=0,
					   font=('Calibri', 11)
					 )

    estilos.configure("tablaBuscar.Treeview.Heading", 
					   background = colorFondo2,
					   foreground = colorLetra,
					   font=('Calibri', 13,'bold')
					 )
                     
    estilos.map("tablaBuscar.Treeview.Heading", 
			     background = [("pressed","darkslateblue"),("active","darkslateblue")]
			   )
	#Remover bordes
    estilos.layout("tablaBuscar.Treeview", 
		            [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]
		          )