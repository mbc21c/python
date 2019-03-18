import sqlite3 as lite
import time

database_filename = 'test.db'
conn = lite.connect(database_filename)
cs = conn.cursor()

#drop table
query = "DROP TABLE IF EXISTS t1"
cs.execute(query)



#create table
query = "CREATE TABLE IF NOT EXISTS t1 (id INTEGER PRIMARY_KEY NOT_NULL, name VARCHAR(255), at DATETIME)"
cs.execute(query)

#insert table
chars = "abcdefghijklmnopqrstuvwxyz"
for a in range(len(chars)):
    query = "INSERT into t1 values (?, ? , DATETIME('NOW'))"
    cs.execute(query,(a, chars[a]))
conn.commit()

#select table
query = "SELECT * FROM t1 WHERE name > 'e';"
cs.execute(query)
all_rows = cs.fetchall()
for i in all_rows:
    print(i)

print("\n" * 3)

#update Table
time.sleep(2)
query = "UPDATE t1 SET name = upper(name), at = DATETIME('NOW') WHERE name > 'r';"
cs.execute(query)
conn.commit()

#check
query = "SELECT * FROM t1;"
cs.execute(query)
all_rows = cs.fetchall()
for i in all_rows:
    print(i)
print("\n" * 3)


#delete
query = "DELETE from t1 WHERE name > 'f';"
cs.execute(query)
conn.commit

#check
query = "SELECT * FROM t1;"
cs.execute(query)
all_rows = cs.fetchall()
for i in all_rows:
    print(i)
print("\n" * 10)


# closig
cs.close()
conn.close()