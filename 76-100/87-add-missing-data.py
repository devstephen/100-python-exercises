checklist = ["Portugal", "Germany", "Spain"]

checklist = [ i + "\n" for i in checklist ]

with open('countries_missing.txt', "r") as file:
    content = file.readlines()

new_list = sorted(checklist + content)

with open("countries_missing_fix.txt", "w") as file:
    for i in new_list:
        file.write(i)
