# new = [new_item for item in list]

numbers = [1,2,3]
new_number = [n+1 for n in numbers]
print(new_number)

name = "Bruno"
lista_letras = [letra for letra in name]
print(lista_letras)

new_range = [n * 2 for n in range(1,5)]
print(new_range)

#CONDITIONAL LIST COMPREHENSION:
# new_list = [*new_item* for *item* in *list* if *test*]

names = ["Bruno", "Pricila", "Benjamim", "Angela"]
nome_curto = [nome for nome in names if len(nome) <6]
print(nome_curto)
nome_longo = [nome.upper() for nome in names if len(nome) >6]  #upper() deixa as letras em maiusculas
print(nome_longo)


#COMPREHENSION DE LIST COM DICIO:
#new_dicio = {new_key:new_value for item in list}

#criar um dicionario e colocar uma nota aleatoria para cada nome abaixo:
import random
names = ["Bruno", "Pricila", "Benjamim", "Angela"]
nota_estudantes = {estudantes: random.randint(1,10) for estudantes in names}
print(nota_estudantes)