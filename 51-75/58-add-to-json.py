import json
from pprint import pprint

new_employee = {
    "firstName": "Albert",
    "lastName": "Bert"
}

new_owner = {
    "firstName": "Jane",
    "lastName": "Duff"
}

# Solution 1

with open('data.json', 'r') as file:
    data = json.loads(file.read())

data["employees"].append(new_employee)

with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)
    

# Solution 2
with open("data.json", "r+") as filename:
    data = json.loads(filename.read())
    data["owners"].append(new_owner)
    filename.seek(0)
    json.dump(data, filename, indent=4, sort_keys=True)
    filename.truncate()