import pandas 

data = pandas.read_csv("https://pythonhow.com/data/sampledata.txt")

data_2 = data * 2

data_2.to_csv("sampledata_x_2.txt", index=None)

print(data)


# Explanation:

# As you can see, this can be done with pandas  in four lines of code. 
# We use read_csv  to create a pandas dataframe object, which is like a table with data. 
# Then we multiply this table by two and then export the calculated data to a text file in our local directory.