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
