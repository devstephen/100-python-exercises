import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

query = "SELECT country FROM countries WHERE area >= 2000000"
cursor.execute(query)
rows = cursor.fetchall()




for i in rows:
    print(i[0])

