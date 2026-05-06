class Numero:
    def __init__(self, dato_numero=0):
        self.dato_numero = int(dato_numero)
    def get_numero(self):
        return self.dato_numero

    def set_numero(self, nuevo_numero):
        self.dato_numero = int(nuevo_numero)

    def validar_numero(self, dato_numero):
        self.set_numero(dato_numero)
        par = "Par" if self.dato_numero % 2 == 0 else "Impar"
        if self.dato_numero > 0: signo = "Positivo"
        elif self.dato_numero < 0: signo = "Negativo"
        else: signo = "Neutro"
        return f"{par} y {signo}"