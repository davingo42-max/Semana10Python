from Vista_formulario import Formulario
from Controlador import ControladorNumero

if __name__ == "__main__":
    controlador = ControladorNumero(Formulario)
    vista = Formulario(controlador) 
    controlador.set_vista(vista)
    vista.iniciar()
