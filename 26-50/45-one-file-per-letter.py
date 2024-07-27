import string, os

letters = string.ascii_lowercase

if not os.path.exists("letters"):
    os.makedirs("letters")


for letter in letters:
    filename = f"letters/{letter}.txt"
    with open(filename, 'w') as f:      
        f.write(letter)



