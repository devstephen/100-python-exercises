from urllib import request


url = "https://pythonhow.com/media/data/universe.txt"



with request.urlopen(url) as response:
    data = response.read().decode('utf-8')

# print(data)


with open('data.txt', 'w') as file:
    file.write(data)