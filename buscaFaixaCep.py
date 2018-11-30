#buscaFaixaCep.py
# encoding: utf-8
''' 
Created By
      _  _____ 
     | |/ ____|
     | | |     
 _   | | |     
| |__| | |____ 
|______v______|                                        
'''

# Importando os dois componentes do preojeto.
from components import Buscador, Menu

# Site dos correrios para requisição
site='http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'

#Criando e preenchendo a tela do projeto
ab = Menu()
ab.corpo()

#Buscando dentro do Menu, o que foi selecionado
arg = str(ab.retorno())
titulo_Arquivo_json = str('Dados/'+arg+'.json')

#Passando como parametro o argumento que foi selecionado no Menu, e o link do site dos correios
#Ao final, concatenando a informações, e transformando os dados em arquivos .json
bcep = Buscador(arg)
bcep.concatena(bcep.busca_Info(site), titulo_Arquivo_json)


