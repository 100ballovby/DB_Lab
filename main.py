import sqlite3

conn = sqlite3.connect('movies.sqlite')
cur = conn.cursor()

res = cur.execute('''
SELECT * FROM movies
''')

for row in res.fetchall():
    print(row[0])

print(res)
