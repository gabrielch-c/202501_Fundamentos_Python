from TarjetaCredito1 import TarjetaCredito

class Usuario:
    def __init__(self, nombre, apellido, email):

        self.nombre = nombre

        self.apellido = apellido

        self.email = email

        self.tarjeta = TarjetaCredito(0, 10000, 0.05)

    def hacer_compra(self):
        self.tarjeta.compra(500)
        print(self.tarjeta.saldo_pagar)

    def pagar_tarjeta(self):
        self.tarjeta.pagar()
        print(self.saldo_pagar)

    def mostrar_saldo_usuario(self):
        self.tarjeta.mostrar_info_tarjeta()
