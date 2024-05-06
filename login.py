import tkinter as tk
from PIL import Image, ImageTk

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        
        # Crear frame izquierdo
        self.frame_izquierdo = tk.Frame(self.root, bg="lightblue", width=200, height=400)
        self.frame_izquierdo.pack(side="left", fill="y")
        
        
        # Colocar el logo en el frame izquierdo
     
        
        image = Image.open(r"C:\Users\Biblioteca\Pictures\1384132495.png")
        image = image.resize((200,100))
        image = ImageTk.PhotoImage(image)
        self.logo = tk.Label(self.frame_izquierdo, image=image,)
        self.logo.place(x=70, y=90)
         
             
        # Crear frame derecho
        self.frame_derecho = tk.Frame(self.root, bg="lightgrey", width=400, height=400)
        self.frame_derecho.pack(side="right", fill="both", expand=True)

        # Titulo de inicio de sesion
        self.titulo_inicio_sesion = tk.Label(self.frame_derecho, text="Inicio de Sesión", font=("Arial", 20))
        self.titulo_inicio_sesion.grid(row=0, column=0, columnspan=2, pady=20)

        # Etiqueta y campo de usuario
        self.label_usuario = tk.Label(self.frame_derecho, text="Usuario:", font=("Arial", 14))
        self.label_usuario.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.entry_usuario = tk.Entry(self.frame_derecho, font=("Arial", 14))
        self.entry_usuario.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Etiqueta y campo de contraseña
        self.label_contrasena = tk.Label(self.frame_derecho, text="Contraseña:", font=("Arial", 14))
        self.label_contrasena.grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.entry_contrasena = tk.Entry(self.frame_derecho, font=("Arial", 14), show="*")
        self.entry_contrasena.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Botón de ingresar
        self.boton_ingresar = tk.Button(self.frame_derecho, text="Ingresar", font=("Arial", 14), command=self.ingresar)
        self.boton_ingresar.grid(row=3, column=0, columnspan=2, pady=20)

    def ingresar(self):
        # Función para manejar el evento de ingreso
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        print("Usuario:", usuario)
        print("Contraseña:", contrasena)

if __name__ == "__main__":
    root = tk.Tk()
    ventana = VentanaPrincipal(root)
    root.mainloop()
    

