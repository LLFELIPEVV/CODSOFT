import tkinter as tk

# Create the main window
ventana = tk.Tk()

ventana.title("Calculadora")
ventana.geometry("500x600")

input = tk.Entry(ventana)
input.pack()

ventana.mainloop()
