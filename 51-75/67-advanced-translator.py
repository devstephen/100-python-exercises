d = dict(weather = "clima", earth = "terra", rain = "chuva") 


def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "We couldn't not find the word"

word = input("Enter word:  ")

print(vocabulary(word))
