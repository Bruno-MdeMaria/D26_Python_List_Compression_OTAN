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

#criar um dicionario comprehension a partir de um dicionario com alunos com media maior que 6 estejam aprovados:
#new_dicio = {new_key:new_value for (key, value) in dict.items() if test}

aprovados = {estudante:nota for (estudante, nota) in nota_estudantes.items() if nota > 6}
print(aprovados)

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}