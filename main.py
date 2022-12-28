import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv") 
dicio = {row.letter: row.code for (index, row) in data.iterrows()}  #a linha index... para receber a coluna (row) cjamda letter e a coluna chamada code.

print(dicio)
#adicionado tratamento de exceção:

def criador_phonetic():
    palavra = input("Escreva uma palavra: ").upper()
    try:    #tentativa:
        soletr = [dicio[letra] for letra in palavra]
    except KeyError:  #exceção que queremos apanhar é uma keyerror.
        print("Desculpe, apenas letras do alfabeto, por favor.")
        criador_phonetic()
    else:#se não ocorrer uma exceção o programa deve apresentar o resultado:
        print(soletr)
criador_phonetic()



