# Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas as pd

phonetic_dict = pd.read_csv('nato_phonetic_alphabet.csv', index_col=0).squeeze("columns").to_dict()
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list  = [phonetic_dict[letter] for letter in word]
print(output_list)

# result = []
# for letter in user_word_list:
#     for (key, value) in data.items():
#         if letter == key:
#             result.append(value)
# print(result)

