from tkinter import *
import sqlite3 as sql
from datetime import date
from PIL import Image, ImageTk
 ## UTILS ##

def centrar_ventana(ventana, anchoVentana, largoVentana):
    ancho = ventana.winfo_screenwidth()
    largo = ventana.winfo_screenheight()
    x = (ancho // 2) - (anchoVentana//2)
    y = (largo // 2) - (largoVentana//2)
    ventana.geometry(f"{anchoVentana}x{largoVentana}+{x}+{y}")


def limpiar_treeview(treeview):
        for item in treeview.get_children():
            treeview.delete(item)

def conectar():
    conexion = sql.connect("BD/ventas.db")
    return conexion

def today():    
    fecha = date.today().strftime("%d/%m/%Y")
    return fecha

def guardar(datos):
    conexion = conectar()
    tabla = conexion.cursor()
    sql = "INSERT INTO Usuarios(nombre, contraseña) VALUES (?,?)"
    tabla.execute(sql, datos)
    conexion.commit()
    tabla.close()

def verificar_existencia_usuario(username, password):
        conexion = conectar()

        tabla = conexion.cursor()

        tabla.execute(f"SELECT nombre, contraseña FROM Usuarios WHERE nombre=?", (username,))

        usuario = tabla.fetchall()
       
        if(usuario[0][0] == username and usuario[0][1] == password):

            conexion.close()
            return True

        conexion.close()
        
def mostrarImagen():
    imagen_pil = Image.open("images/login.png")
        
        

