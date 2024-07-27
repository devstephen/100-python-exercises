import string

filename = 'letter-by-two.txt'

with open(filename, 'w') as file:
    letters = string.ascii_lowercase
    for pair in zip(letters[::2], letters[1::2]):
        file.write(''.join(pair) + '\n')