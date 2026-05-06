import tkinter as tk
from tkinter import messagebox

class Formulario:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.titulo = "¡ANALICEMOS TU NUMERO!"
        self.root.geometry("300x300")
        self.root.title(self.titulo)
        
        tk.Label(self.root, text="¿Cuál es su número?").pack()
        self.campo_dato_numero = tk.Entry(self.root)
        self.campo_dato_numero.pack()
        
        tk.Button(self.root, text="Analizar", command=self.pedir_numero).pack()

    def pedir_numero(self): 
        valor = self.campo_dato_numero.get()
        self.controlador.tomar_numero(valor)

    def imprimir_mensaje(self, mensaje): 
        messagebox.showinfo("Resultado", mensaje)
        
    def mostrar_error(self, error):
        messagebox.showerror("Error", error)