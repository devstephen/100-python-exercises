import sqlite3, pandas

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

query = "SELECT * FROM countries WHERE area >= 2000000"
cursor.execute(query)
rows = cursor.fetchall()
conn.close()


df = pandas.DataFrame.from_records(rows)
df.columns = [ "Rank", "Country", "Area", "Population" ]
df.to_csv("countries_from_db.csv", index=False)