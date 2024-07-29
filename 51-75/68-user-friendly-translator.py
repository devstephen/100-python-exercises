d = dict(weather = "clima", earth = "terra", rain = "chuva") 


def vocabulary(word):
   try:
      return d[word]
   except KeyError:
      return "We couldn't find that word"

word = input("Enter word:  ").lower()
# small_letter = word.lower()

print(vocabulary(word))

# Explanation:

# As you see, we are converting all the string characters to lowercase as soon as we receive the user's input. 
# Then we pass the lowercase version of the string to the dictionary.