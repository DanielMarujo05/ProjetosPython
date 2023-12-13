class Conta:
    def __init__(self,titular,numero,saldo):
        self._saldo=saldo
        self._numero=numero
        self._titular=titular

    def saque(self,valor):
        if self._saldo>=valor:
            self._saldo-=valor
            print("saque realizado com sucesso!!")
        else:
            print("valor do saldo insuficiente")

    def deposita(self,valor):
        self._saldo+=valor

    def extrato(self):
        print("Cliente:",self._titular,"\nSaldo Atual: ",self._saldo)

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,saldo):
        if (saldo<0):
            print("o saldo nao pode ser negativo")
        else:
            self._saldo=saldo