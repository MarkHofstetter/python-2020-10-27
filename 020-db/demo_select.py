import sqlite3

conn = sqlite3.connect("students.db")

search_name = input("namen eingeben: ")

# BÖSE!!!
# sql = 'SELECT * FROM student WHERE name ="' + search_name + '"'

# nur mit bind variablen Wert vom User übernehmen
cursor = conn.execute('select * from student WHERE name = ?', (search_name,) )
for row in cursor:
    print(row)
    
conn.close()