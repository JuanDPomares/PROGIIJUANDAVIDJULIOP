import tkinter as tk
def registrar():
    frame = tk.Label(coco, text = torombolo.get())
    frame= tk.Label(coco, text = macaco.get())
    frame.pack()

ventana = tk.Tk()
ventana.title("monocuco")
ventana.geometry("800x600")
ventana.resizable(True, True)
colacao = tk.Label(ventana, text="trululu: ")
colacao.place(x=5, y=10)
torombolo = tk.Entry(ventana, width = 30)
torombolo.place(x=50, y=10 )

macaco = tk.Label(ventana, text="cuenta bancaria:")
macaco.place(x=5, y=40)
macaco = tk.Entry(ventana, width= 30)
macaco.place(x= 100, y=40)


registrar= tk.Button(ventana, text="regitrar", command=registrar)
registrar.place(x=10, y=70)

coco = tk.Frame(ventana, width=300, height=150, relief="raised", bd = 1, bg = "white")
coco.place(x=30, y= 100)


ventana.mainloop()
