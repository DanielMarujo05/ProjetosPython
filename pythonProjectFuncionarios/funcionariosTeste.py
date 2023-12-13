from funcionarios import Funcionarios

funcionario=Funcionarios('Gabriela','gabriela.silva2000@gmail.com')

funcionario.cadastro_hora('jan',300)
funcionario.cadastro_hora('fev',200)
funcionario.cadastro_salario_hora('jan',30)
funcionario.cadastro_salario_hora('fev',20)

print(funcionario)
print(funcionario.calcula_salario('jan'))
print(funcionario.calcula_salario('fev'))