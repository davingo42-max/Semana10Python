import tkinter as tk
from Vista_formulario import Formulario
from Controlador import ControladorNumero

if __name__ == "__main__":
    root = tk.Tk()
    
    controlador = ControladorNumero(Formulario)
    
    vista = Formulario(root, controlador)
    
    controlador.set_vista(vista)
    
    root.mainloop()