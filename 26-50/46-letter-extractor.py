import glob


letters = []

file_list = glob.glob("letters/*.txt")
print(file_list)
for filename in file_list:
    with open(filename, 'r') as file:
       letter = file.read()
       letters.append(letter)

print(letters) 