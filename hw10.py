import sqlite3 as sql
connection = sql.connect('Base.sl3', 5)
cur = connection.cursor()
cur.execute('DROP TABLE bank')
cur.execute('CREATE TABLE bank (id TNT, f_name TEXT,l_name TEXT, mon INT)')


cur.execute('INSERT INTO bank VALUES(1, "asdfgafg", "luherg", 45000)')
cur.execute('INSERT INTO bank VALUES(2, ";uasg", "klhguh", 150000)')
cur.execute('INSERT INTO bank VALUES(3, ";uigarf", "ariohg", 1530580)')
cur.execute('INSERT INTO bank VALUES(4, "a;garg", "arasgafsg", 8000000)')
cur.execute('INSERT INTO bank VALUES(5, "as;kjg", "agjufg", 7890000)')
cur.execute('Select * from bank')


res = cur.fetchall()
print(res)
connection.commit()
connection.close()

