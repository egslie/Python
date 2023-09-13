"""Descrição: Faça um algoritmo que leia 100 números e retorne a média desses valores."""

numero = int 
media = float
soma = float

numero =  0
soma = 0
while numero < 100:
    print("Digite seu número:")
    valor = float(input());
    
    soma += valor
    numero += 1
    
    media = soma/numero
    
    print("Soma:", soma)
    print("Média:", media)