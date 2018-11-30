#busca_cep.py
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
'''
	Com o intuito de capturar dados dos sites dos correios, 
A classe BUSCADOR, inicia todo o processo, fazendo a requisição 
ao banco dos correios, e trazando a informação completa, em formato
html.
	Após obter resposta da requisição, trabalhamos os dados nos metodos
para dispensar as tags e dados indesejados, e manternos nas listas, somente
as informações interessantes a concatenação
'''

import requests
from bs4 import BeautifulSoup
import urllib3
import json


class Buscador:

	def __init__(self,estado):
		self.est = estado
# Buscando informções no site dos correios
	def busca_Info(self,url):

		# Parametros para requisição, conforme particularidade do site dos correios, na url que foi passada no ambiente principal
		post_fixed = {'UF': self.est, 'Localidade':'', 'qtdrow':'100', 'pagini':'1', 'pagfim':'101'}

		#Instanciando o Objeto e guardando o resultado da requisição na variavel r
		http = urllib3.PoolManager()
		r = http.request('POST', url=url, fields=post_fixed)

		#Transformando os dados coletados na requisição para a Biblioteca BeautifulSoup
		soup = BeautifulSoup(r.data, 'lxml')
		return soup.find_all('table', class_='tmptabela')

	#Minerando e dividindo os dados das cidades
	def separador_cidades(self,lista_dados):

			lista_dados_cidades = []

			for lt in lista_dados:
				lista_cidades = lt.find_all('td', attrs={'width':'100'})

			for lcidades in lista_cidades:
				if lcidades.next_element != 'Não codificada por logradouros' and lcidades.next_element != 'Codificado por logradouros' and lcidades.next_element != 'Codificada por logradouros':
					lista_dados_cidades.append(str('{0}' .format(lcidades.next_element)))
			return lista_dados_cidades


	#Minerando e dividindo os dados do cep
	def separador_cep(self,lista_dados):

		lista_dados_cep = []

		for lt in lista_dados:
			lista_cep = lt.find_all('td', attrs={'width':'80'})

		for lcep in lista_cep:
			lista_dados_cep.append(str('{0}' .format(lcep.next_element))) 

		return lista_dados_cep



	#Gerando um arrey com os dados e gravando os arquivos no json
	def grava_arquivo_json(self,titulo_do_Arquivo, estado, lt_cidades, lt_cep):

		n = 0
		arq_json = open(titulo_do_Arquivo, 'w')
		while n != len(lt_cep):
			lista_salvar = [dict(cep=lt_cep[n], cidade=lt_cidades[n])]
			n += 1
			dict_salvar = {'Cidades de '+estado : lista_salvar}
			dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)

			try:
				arq_json.write(dict_salvar)

			except Exception as erro:
				print("Erro ao carregar o arquivo")
				print("O erro ŕ: {}".format(erro))
				break

		arq_json.close()

	# Metodo criado para simplicar a passagem de parametros
	def concatena(self, lista_completa, t_json):
		l_cidade = self.separador_cidades(lista_completa)
		l_cep = self.separador_cep(lista_completa)
		self.grava_arquivo_json(t_json, self.est, l_cidade, l_cep )


