import tkinter as tk
ventana = tk.Tk()
Fsexo =  tk.IntVar()

def registrar():
    pass

def obtener_eleccion():
    seleccion = Fsexo.get()
    if seleccion == 1:
        print("Opción 1 seleccionada")
    elif seleccion == 2:
        print("Opción 2 seleccionada")
    
opcion1 = tk.Radiobutton(ventana, text="Opción 1", variable=Fsexo, value=1, command=obtener_eleccion)
opcion1.pack()


opcion2 = tk.Radiobutton(ventana, text="Opción 2", variable=Fsexo, value=2, command=obtener_eleccion)
opcion2.pack()




ventana.title("Datos de Persona")

ventana.geometry("800x600")


ventana.resizable(True,True)

Fnombre = tk.Label(ventana, text="nombre: ")
Fnombre.grid(row=0, column=0)
Cnombre = tk.Entry(ventana, width=20)
Cnombre.grid(row=0, column=1)

Fapellido = tk.Label(ventana, text="apellido: ")
Fapellido.grid(row=1, column=0)
Capellido = tk.Entry(ventana, width=20)
Capellido.grid(row=1, column=1)

Fedad = tk.Label(ventana, text="edad: ")
Fedad.grid(row=2, column=0)
Cedad = tk.Entry(ventana, width=20)
Cedad.grid(row=2, column=1)


Ftelefono = tk.Label(ventana, text="telefono: ")
Ftelefono.grid(row=3, column=0)

Fciudad = tk.Label(ventana, text="ciudad: ")    
Fciudad.grid(row=4, column=0)

Fdireccion = tk.Label(ventana, text="direccion: ") 
Fdireccion.grid(row=5, column=0)

Fsexo = tk.Label(ventana, text="sexo: ")
Fsexo.grid(row=6, column=0)




ventana.mainloop()
