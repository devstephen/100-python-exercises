checklist = ["Portugal", "Germany", "Munster", "Spain"]
def data_checker():
    with open('countries_clean.txt', "r") as file:
        countries = file.readlines()
        cleaned_countries = [ i.rstrip('\n') for i in countries ]
        checked_countries = [c for c in cleaned_countries if c in checklist]
        print(checked_countries)

data_checker()

