import sqlite3, pandas

data = pandas.read_csv("ten_more_countries.txt")

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

for index, row in data.iterrows():
    print(row["Country"], row["Area"])
    cursor.execute("INSERT INTO countries VALUES (NULL, ?, ?, NULL)", (row["Country"], row["Area"]))
conn.commit()
conn.close()