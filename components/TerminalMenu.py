#TerminalMenu.py
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
	Com o Objetivo de facilitar a experiencia do usuario,
e a reutilização do código, um menu interativo pode facilitar
a compreenssão do  objetivo a qual o codigo se propoe
'''
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import time
from components import Buscador

# Classe criada para importar os objetos
class Menu:


	#Metodo que valida as informações no form gerado
	def obter(self):

		global result
		
		result = combo.get()

		if result == "":
			ask = messagebox.askokcancel(title="Erro", message="Voce Precisa Escolher um Estado(UF)")
			if ask == True: 
				quadro.destroy()
				self.corpo()
			quadro.destroy()
		else:
			messagebox.showinfo("BuscaCEP", "Concluido com Sucesso!")
			quadro.destroy()
			
	#Metodo criado para transferir a variavel com o valor selecionado entre os objetos
	def retorno(self):
		return result

	#Metodo que cria o form com tkinter, implemente as variaveis globais
	def corpo(self):

		global quadro, combo

		#Criando o fundo do quadro
		quadro =  Tk()
		quadro.geometry("430x300")
		quadro.title('Busca Cep')


		#Criando o componente definido combobox, e preenchendo com as informações do estado
		combo = ttk.Combobox(quadro)
		combo.place(x=65, y=170)
		combo['values'] = ("AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", 
		"SE", "SP", "TO")


		#Criando os componentes de Texto e Botoes;
		button = Button(quadro, command=self.obter, text='BuscarCEP')
		button.place(x=260, y=165)
	
		label2 = Label(quadro, text="Escolha um Estado:")
		label2.place(x=65, y=150)

		label3 = Label(quadro, text="Escolha o Estado que deseja obter os dados,\nClique em BuscarCEP, e os dados serão armazenados \ndentro da pasta Dados/ no projeto.")
		label3.place(x=50, y=70)


		quadro.mainloop()

