"""Descrição: Elaborar um programa que permita ler um número a partir do teclado, e apresentar a indicação de que é positivo, negativo ou nulo.
Entradas: Números
Saídas: mensagens descricões do problema:
Se N=0 então N é nulo
Se N>0 então N é positivo
Senão N é negativo."""

numero=int (input("Digite o números que você quer análisar:"))

if numero == 0:
		print("Seu número é NULO")

if numero > 0:
		print("Seu número é POSITIVO")

else:
		print("Seu número é NEGATIVO")


