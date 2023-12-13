#Utilizando funcionalidades como biblioteca

from funcionalidades import *

tv=Tv("Philco",'philco-2013')

controle= Controle(tv)

controle.sintonizaCanal("globo")

controle.trocaCanal("globo")

print(tv.canal_atual)