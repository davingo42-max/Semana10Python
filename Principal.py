import tkinter as Ventana
from Vista_formulario import Formulario
from Controlador import ControladorNumero

if __name__ == "__main__":

    root = Ventana.Tk()

    controlador = ControladorNumero(Formulario)
    vista = Formulario(root, controlador)
    controlador.set_vista(vista)
    root.mainloop()