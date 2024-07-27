def counter(str):
    count = str.split()
    return len(count)

print(counter("men will always be men"))

# Explanation:

# We're using split  here which is a string method that splits a string into several strings given a separator passed inside the brackets. 
# When you don't pass a separator, split  will split a string at white spaces. 
# This will output a list of strings..
# Applying len  to that list returns the number of list items, so the number of words.