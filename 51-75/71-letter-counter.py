from urllib import request


url = "https://pythonhow.com/media/data/universe.txt"



with request.urlopen(url) as response:
    data = response.read().decode('utf-8')

char_count = data.count("a")

print(char_count)
