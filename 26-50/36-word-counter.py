def words_counter(file):
    with open(file, 'r') as file_path:

        content = file_path.read()
        words_split = content.split()

    return len(words_split)

print(words_counter(r"C:\Users\ndifreke\Desktop\100-python-projects\26-50\words1.txt"))

# Explanation:

# The function here takes as input a file path. If the file path is in the same directory as your Python script, you can pass in the file name as in the above script. 
# If your text file is somewhere else, then you need to pass the full path when calling the function. 
# Example: print(count_words("C:/Home/words1.txt"))
# The rest of the script consists of opening the file in read  mode, loading the text into a string using read  and then splitting and counting the number of words.