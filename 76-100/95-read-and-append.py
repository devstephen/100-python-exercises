line = input("Enter values:  ")

line_list = line.split(",")

with open("planets.txt", "a+") as file:
    for i in line_list:
        file.write(i + "\n")