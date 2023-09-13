"""Descrição: Problema; Controlar o acesso a uma porta usando uma senha pré-configurada no sistema.
Dado de Entrada; Senha(variável alfanumérica)
Dado de Saída: Porta Aberta (simulado com mensagem "PORTA ABERTA") ou mensagem de "SENHA NÃO CONFERE"
Variáveis: Senha (Tipo alfanumérica)"""

from IPython.display import clear_output

senhaCadas = input("Digite sua senha para sempre ter acesso ao sistema:")
senhaLogin = input("Digite a sua senha para ter acesso ao Banco de Dados:")

clear_output(wait=True)

if senhaCadas==senhaLogin:

		print("Seja Bem-Vind@ Funcionário 1!")
		print("")
		print("PORTA ABERTA!")

else:

		print("ERRO!")
		print("Senha incorreta, reinicie o sistema!")
