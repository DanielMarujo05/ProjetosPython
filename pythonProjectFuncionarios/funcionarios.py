class Funcionarios:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
        self.horas={}
        self.salario_hora={}

    def cadastro_hora(self,mes,horas):

        if mes not in self.horas:
            self.horas[mes]=horas

    def cadastro_salario_hora(self,mes,valor):

        if mes not in self.salario_hora:
            self.salario_hora[mes]=valor

    def calcula_salario(self,mes):

        if mes not in self.horas or mes not in self.salario_hora:
            print("mes inesistente!")
            return None
        else:
            return self.horas[mes]*self.salario_hora[mes]

    def __repr__(self):

        return f'Funcionário: {self.nome},\nemail: {self.email},\nhoras/mes: {self.horas},Salario/hora: {self.salario_hora}'
