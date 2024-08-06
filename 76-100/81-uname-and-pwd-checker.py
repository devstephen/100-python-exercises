while True:
    usr = input("Enter username:  ")
    with open("users.txt", "r") as file:
        users = file.readlines()
        users = [ i.strip("\n") for i in users ]
    if usr in users:
        print("Username already exists")
        continue
    else:
        print("Username is available")
        break        


while True:
    notes = []
    pwd = input("Enter password  ")

    if not any(i.isdigit() for i in pwd):
        notes.append("Password must contain at least one number")

    if not any(i.isdigit() for i in pwd):
        notes.append("Password must contain at least one uppercase letter")
    if len(pwd) < 5:
        notes.append("Password must contain at least five characters")

    if len(notes) == 0:
        print("Password is valid")
        break
    else:
        print("Pleck check the following: ")
        for note in notes:
            print(note)