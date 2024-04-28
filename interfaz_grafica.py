import tkinter as tk 
from PIL import Image, ImageTk
def cambiar_texto():
    etiqueta.config(text="Texto cambiado")
def obtener_texto():
    texto_ingresado = cuadro_texto.get()
    if texto_ingresado:
        etiqueta.config(text="Texto ingresado: " + texto_ingresado)
    else:
        etiqueta.config(text="No se ha ingresado texto", bg="grey", relief="groove")
def obtener_seleccion():
    seleccion = variable.get()
    if seleccion == 1:
        print("Opción 1 seleccionada")
    elif seleccion == 2:
        print("Opción 2 seleccionada")
    elif seleccion == 3:
        print("Opción 3 seleccionada")
        
def obtener_seleccion2():
    seleccion2 = variable2.get()
    if seleccion2 == 1:
        print("Opción 1 seleccionada")
    elif seleccion2 == 2:
        print("Opción 2 seleccionada")
    elif seleccion2 == 3:
        print("Opción 3 seleccionada")
def obtener_seleccion3():
    seleccion3 = variable3.get()
    if seleccion3 == 1:
        print("Opción 1 seleccionada")
    elif seleccion3 == 2:
        print("Opción 2 seleccionada")
    elif seleccion3 == 3:
        print("Opción 3 seleccionada")
        
ventana = tk.Tk()
path = Image.open(r"C:\Users\Admin\Pictures\estelar.jpg")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)
ventana.title("Cosmos")
ventana.geometry("500x500")
Imagen_Label = tk.Label(ventana, image=icono)
Imagen_Label.pack()
Imagen_Label.config(width=500, height=500)
Imagen_Label.place(x=0, y=1)

ventana.resizable(True,True)
etiqueta = tk.Label(ventana, text="cual es el nombre de este objeto: ", bg="grey")
etiqueta.pack()
cuadro_texto = tk.Entry(ventana, width=30)
cuadro_texto.pack()
boton = tk.Button(ventana, text="Obtener Texto", command=obtener_texto, bg="grey", relief="groove")
boton.pack()



variable = tk.IntVar()
etiqueta2 = tk.Label(ventana, text="como se le llama al brillo alrededor del objeto?: ", bg="grey", relief="groove")
etiqueta2.pack()


opcion1 = tk.Radiobutton(ventana, text="Disco de acresion", variable=variable, value=1, command=obtener_seleccion, bg="grey", relief="groove")
opcion1.pack()

opcion2 = tk.Radiobutton(ventana, text="Dona", variable=variable, value=2, command=obtener_seleccion, bg="grey", relief="groove")
opcion2.pack()

opcion3 = tk.Radiobutton(ventana, text="anillo", variable=variable, value=3, command=obtener_seleccion, bg="grey", relief="groove")
opcion3.pack()
opcion4 = tk.Radiobutton(ventana, text="tornado", variable=variable, value=4, command=obtener_seleccion, bg="grey", relief="groove")
opcion4.pack()

etiqueta3 = tk.Label(ventana, text="Cuantos lados tiene este objeto? ", bg="grey", relief="groove")
etiqueta3.pack()
variable2 = tk.IntVar()
opcion4 = tk.Radiobutton(ventana, text="2", variable=variable2, value=1, command=obtener_seleccion2, bg="grey", relief="groove")
opcion4.pack()

opcion5 = tk.Radiobutton(ventana, text="7", variable=variable2, value=2, command=obtener_seleccion2, bg="grey", relief="groove")
opcion5.pack()

opcion6 = tk.Radiobutton(ventana, text="1", variable=variable2, value=3, command=obtener_seleccion2, bg="grey", relief="groove")
opcion6.pack()

opcion7 = tk.Radiobutton(ventana, text="inf", variable=variable2, value=4, command=obtener_seleccion2, bg="grey", relief="groove")
opcion7.pack()

variable3 = tk.IntVar()
etiqueta4 = tk.Label(ventana, text="Porqué se producen? ", relief="sunken", bg="grey")
etiqueta4.pack()


opcion7 = tk.Radiobutton(ventana, text="mucha masa concentrada en un espacio pequeño", variable=variable3, value=1, command=obtener_seleccion2, relief="groove", bg="grey")
opcion7.pack()

opcion8 = tk.Radiobutton(ventana, text="estrella explotando", variable=variable3, value=2, command=obtener_seleccion2, relief="groove", bg="grey")
opcion8.pack()

opcion9 = tk.Radiobutton(ventana, text="imposible saber", variable=variable3, value=3, command=obtener_seleccion2, relief="groove", bg="grey")
opcion9.pack()




ventana.mainloop()