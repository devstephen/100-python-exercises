def word_counter(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

        text = file_content.replace(",", " ")

        split_content = text.split()

    return len(split_content)

print(word_counter(r'C:\Users\ndifreke\Desktop\100-python-projects\26-50\words2.txt')) 

# This solution is like the previous exercise's solution with the difference that before splitting, 
# we are replacing all commas with a space that will let the split method count the number of words.

import re

def count_words(filepath):
    with open(filepath, 'r') as file_location:
        text = file_location.read()

        string_list = re.split(",| ", text)

        return len(string_list)
    
print(count_words(r"C:\Users\ndifreke\Desktop\100-python-projects\26-50\words2.txt"))



# This alternative solution uses the built-in re  module, 
# which provides regular expression matching operations. 
# We're using the split method of that module, and the expression ",| " is meant to replace commas with spaces. 
# Using methods from the re  module can be more appropriate than Python built-in methods when string operations are complicated. 
# However, for this simple scenario, the re  module could be skipped.