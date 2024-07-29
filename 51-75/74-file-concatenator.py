import pandas 

file1 = pandas.read_csv("https://pythonhow.com/data/sampledata.txt")
file2 = pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")

new_data = pandas.concat([file1, file2])

new_data.to_csv("new_sample.txt", index=None)

# Explanation

# Again we are using pandas to load the data into Python. 
# Then in line 5, we use the concat  method. 
# The method expects as input a list of dataframe objects to be concatenated. 
# Lastly, in line 6, we export the data to a new text file.