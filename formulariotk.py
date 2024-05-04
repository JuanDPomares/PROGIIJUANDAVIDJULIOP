import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()

def registrar():
    nombre = Cnombre.get()
    apellido = Capellido.get()
    edad = Cedad.get()
    direccion = Cdireccion.get()
    genero = obtener_genero()
    ciudades = obtener_ciudades()
    telefono = Ctelefono.get()
    mensaje = f"Información registrada:\n\n"
    mensaje += f"Nombre: {nombre}\n"
    mensaje += f"Apellido: {apellido}\n"
    mensaje += f"Edad: {edad}\n"
    mensaje += f"Dirección: {direccion}\n"
    mensaje += f"Género: {genero}\n"
    mensaje += f"Teléfono: {telefono}\n"
    mensaje += f"Ciudades seleccionadas: {', '.join(ciudades)}"
    messagebox.showinfo("Información Registrada", mensaje)

def obtener_ciudades():
    seleccionados = cuadro_lista.curselection()
    ciudades = [cuadro_lista.get(index) for index in seleccionados]
    return ciudades

def obtener_genero():
    seleccion = Csexo.get()
    if seleccion == 1:
        print("Opción 1 seleccionada")
        return "Masculino"
    elif seleccion == 2:
        print("Opción 2 seleccionada")
        return "Femenino"

Csexo = tk.IntVar()
opcion1 = tk.Radiobutton(ventana, text="Masculino", variable=Csexo, value=1, command=obtener_genero)
opcion1.grid(row=7, column=0)

opcion2 = tk.Radiobutton(ventana, text="Femenino", variable=Csexo, value=2, command=obtener_genero)
opcion2.grid(row=7, column=1)

ventana.title("Datos de Persona")
ventana.geometry("800x600")
ventana.resizable(True, True)

Fnombre = tk.Label(ventana, text="Nombre:")
Fnombre.grid(row=0, column=0)
Cnombre = tk.Entry(ventana, width=20)
Cnombre.grid(row=0, column=1)

Fapellido = tk.Label(ventana, text="Apellido:")
Fapellido.grid(row=1, column=0)
Capellido = tk.Entry(ventana, width=20)
Capellido.grid(row=1, column=1)

Fedad = tk.Label(ventana, text="Edad:")
Fedad.grid(row=2, column=0)
Cedad = tk.Entry(ventana, width=20)
Cedad.grid(row=2, column=1)

Ftelefono = tk.Label(ventana, text="Teléfono:")
Ftelefono.grid(row=3, column=0)
Ctelefono = tk.Entry(ventana, width=20)
Ctelefono.grid(row=3, column=1)

Fciudad = tk.Label(ventana, text="Ciudad:")
Fciudad.grid(row=4, column=0)
cuadro_lista = tk.Listbox(ventana, width=30, selectmode="multiple")
cuadro_lista.grid(row=4, column=1)
ciudad = ["Cartagena", "Medellin", "Barranquilla", "San Fernando"]
for item in ciudad:
    cuadro_lista.insert(tk.END, item)

Fdireccion = tk.Label(ventana, text="Dirección:")
Fdireccion.grid(row=5, column=0)
Cdireccion = tk.Entry(ventana, width=20)
Cdireccion.grid(row=5, column=1)

Fsexo = tk.Label(ventana, text="Sexo:")
Fsexo.grid(row=6, column=0)

tk.Button(ventana, text="Registrar", command=registrar).grid(row=8, column=1, padx=5, pady=5)

ventana.mainloop()
