import mysql.connector as myconn

mydb=myconn.connect(user='root', host='localhost', password='9595946682', database= 'legion') 

db_cursor=mydb.cursor()
db_cursor.execute('show tables ') 

for i in db_cursor:
    print(i)
      
print("succesfully ")  

