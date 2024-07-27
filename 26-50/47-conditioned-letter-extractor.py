import glob

file_list = glob.iglob("letters/*.txt")
letters = []
check = 'python'

for file in file_list:
    with open(file, 'r') as file:
        letter =  file.read()
    if letter in check:
        letters.append(letter)
print(letters)


# Explanation:

# The glob module here helps to generate a list of text files. 
# Then we iterate through that list and read each file inside the loop, strip "\n" characters 
# and then check if the letter extracted from the file is in the string "python," 
# and we append that letter if it is.