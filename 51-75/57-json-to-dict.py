import json
from pprint import pprint

with open('data.json', 'r') as file:
    data = json.loads(file.read())
    

pprint(data)