import string

filename = 'alphabet.txt'

with open(filename, 'w') as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")