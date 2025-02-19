class TarjetaCredito:


    def __init__(self, saldo_pagar, limite_credito, intereses):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

    def compra(self, monto):
        if monto > self.limite_credito :
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
            self.limite_credito -= monto
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self
    

    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: {self.saldo_pagar}")

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

tarjeta1 = TarjetaCredito(0, 10000, 0.02)
tarjeta1.compra(500).compra(200).pago(300).cobrar_interes().mostrar_info_tarjeta()

tarjeta2 = TarjetaCredito(0, 10000, 0.05)
tarjeta2.compra(3000).compra(2000).compra(1000).pago(2500).pago(1000).cobrar_interes().mostrar_info_tarjeta()

tarjeta3 = TarjetaCredito(0, 10000, 0.03)
tarjeta3.compra(5000).compra(1000).compra(2000).compra(1000).compra(3000)