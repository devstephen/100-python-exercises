from pprint import pprint

d = dict( a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)) )

for key, values in d.items():
    print(key, "has values", values)