d = dict(weather = "clima", earth = "terra", rain = "chuva") 


def vocabulary(word):
    return d[word]

word = input("Enter word:  ")

print(vocabulary(word))

# Explanation:

# It's good to create a function as the above code shows so that the code is more organized in case you need to expand it and add more features later. 

# The function gets the word string from the input  function, queries the dictionary and prints out the result. 
# Of course, we are forced to use only the words we have in the dictionary. 
# If you want to make this a more real-life translator, you would need a complete dictionary, 
# and you would also want to store it in a file instead of keeping it inside the script. 