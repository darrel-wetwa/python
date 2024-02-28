import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES(1,'FAITH KARIMI',23,354000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(2,'BOB KURIA',19,450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(3,'NELSON MANDELA',27,600000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(4,'JANE WAITHERA',32,700000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(5,'JULIUS OCHIENG',45,320000.00)")

conn.commit()
print("records inserted successfully")
conn.close()