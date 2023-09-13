"""
nome = []
nome = str(input("Qual o nome do grupo de kpop?"))
 

for _ in range(nome):
    digitar = input("Deseja continuar?")
    nome.append(digitar)

print("Nomes:", nome)

print("Deseja adicionar o nome de um grupo de kpop?")
digitar =  str
while digitar != "não":
    digitar = str(input())"""
    
atrizes = ["Paolla de Oliveira"]
atrizes.append("Camila Queiroz")
while True:
    nome = input("Digite o nome de uma atriz:")
    atrizes.append(nome)
    resp =  input("Deseja continuar [S/N]?")
    if resp.upper()== "N":
        break
    print(atrizes)
 
 """atizes = ["Paolla de Oliveira"]
    atrizes.append("Sheron Menezes")
    atrizes.insert(1,"Raquel Nunes")
    print(atrizes)"""      
    