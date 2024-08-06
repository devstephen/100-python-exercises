from datetime import datetime 

current_year = datetime.now().year
age = int(input("How old are you?   "))

user_yob = current_year - age


print(f"We think you were born in {user_yob}")