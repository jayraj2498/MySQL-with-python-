# how to see the record in our python terminal 

import mysql.connector as myconn

mydb = myconn.connect(user='root', host='localhost', password='9595946682', database='legion')

db_cursor = mydb.cursor() 

db_cursor.execute('select * from family') 

for record in db_cursor.fetchall() :
    print(record)  



