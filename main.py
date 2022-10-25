import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv") 
dicio = {row.letter: row.code for (index, row) in data.iterrows()}  #a linha index... para receber a coluna (row) cjamda letter e a coluna chamada code.

palavra = input("Escreva uma palavra: ").upper()
soletr = [dicio[letra] for letra in palavra]
print(soletr)



