class Usuario:
    def __init__(self, nombre, apellido, email):

        self.nombre = nombre

        self.apellido = apellido

        self.email = email

        self.limite_credito = 30000

        self.saldo_pagar = 0


    def hacer_compra(self, monto: int):
        self.saldo_pagar += monto
        print("su saldo a pagar es de ", str(self.saldo_pagar))
        self.limite_credito -= monto
        print(f"Su limite de crédito es de {self.limite_credito}")

    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto
    
    def mostrar_saldo_usuario(self):
        print(f"Usuario {self.nombre} {self.apellido}, Saldo a pagar: {self.saldo_pagar}") 



miUsuario = Usuario("gabo","chirinos", "gabochi")
print(miUsuario.hacer_compra(300))
print(miUsuario.pagar_tarjeta(100))
print(miUsuario.mostrar_saldo_usuario())