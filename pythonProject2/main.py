class main:
    pass

print('Testando o projeto')

from cliente import Cliente

from NomeConta import Conta

c1=Cliente("Fernando", "95437-8473")

conta=Conta(c1._nome,6000,150)

print("titular:",conta._titular,"\nnumero:",conta._numero,"\nsaldo:",conta._saldo)

conta.deposita(100)
print("\n")
conta.saque(100)
print("\n")
conta.extrato()


