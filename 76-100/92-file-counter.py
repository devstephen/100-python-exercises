import glob


# pattern = os.path.join('./files', "*.py")

py_files = glob.glob1('./files', "*.py")

print(f"There are {len(py_files)} Python files in the folder")

# Explanation:

# We're using glob  which is a standard Python library that finds pathnames matching a specified pattern. 
# From glob  we're using glob1  which takes a directory name as the first argument and a pattern which in our case is *.py  
# which returns all the files starting with whatever and ending with .py in the files  directory.