import glob




py_files = glob.glob("subdirs/**/*.py", recursive=True )

print(f"There are {len(py_files)} Python files in this directory and its subdirectories")

# Explanation:

# We're using glob.glob  in contrast to glob.glob1 , gets a pathname pattern and a recursive  argument, 
# which indicates whether you want to search sub-directories or not.