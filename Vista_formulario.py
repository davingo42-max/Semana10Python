import tkinter as Ventana
from tkinter import messagebox

class Formulario:
    def __init__(self, controlador): 
        self.root = Ventana.Tk() 
        self.controlador = controlador
        self.titulo = "¡ANALICEMOS TU NUMERO!"
        self.root.geometry("300x300")
        self.root.title(self.titulo)
        
        Ventana.Label(self.root, text="¿Cual es su número?").pack()
        self.campo_dato_numero = Ventana.Entry(self.root)
        self.campo_dato_numero.pack()
        
        Ventana.Button(self.root, text="Analizar", command=self.pedir_numero).pack()

    def iniciar(self):
        self.root.mainloop()

    def pedir_numero(self): 
        valor = self.campo_dato_numero.get()
        self.controlador.tomar_numero(valor)

    def imprimir_mensaje(self, mensaje): 
        messagebox.showinfo("Resultado", mensaje)
        
    def mostrar_error(self, error):
        messagebox.showerror("Error", error)
