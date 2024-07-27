import string

filename = 'letter-by-three.txt'


with open(filename, 'w') as file:
    letters = string.ascii_lowercase + " "
    for letter in zip(letters[0::3], letters[1::3], letters[2::3]):
        file.write(''.join(letter) + '\n')