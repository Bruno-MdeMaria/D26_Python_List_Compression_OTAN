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

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv") 
dicio = {row.letter: row.code for (index, row) in data.iterrows()}  #a linha index... para receber a coluna (row) cjamda letter e a coluna chamada code.
print(dicio)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
palavra = input("Escreva uma palavra: ").upper()
phonetic = [dicio[letter] for letra in palavra]
print(phonetic)




