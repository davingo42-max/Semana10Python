from Numero import Numero

class ControladorNumero:

    def __init__(self, vista_clase):
        self.obj_numero = Numero() 
        self.obj_vista = None      

    def tomar_numero(self, valor): 
        resultado = self.obj_numero.validar_numero(valor)
        self.imprimir_numero(resultado)

    def imprimir_numero(self, mensaje):
        self.obj_vista.imprimir_mensaje(mensaje)

    def set_vista(self, vista):
        self.obj_vista = vista