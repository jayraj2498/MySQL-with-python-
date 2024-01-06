import mysql.connector as myconn 
mydb=myconn.connect(host='localhost',user='root',password='9595946682',database='legion') 

db_cursor=mydb.cursor() 

db_delete='delete from family where f_name=%s'
db_value=('jayraj',)

db_cursor.execute(db_delete,db_value) 
mydb.commit() 

print(db_cursor.rowcount,"row deleted")  




# import mysql.connector as myconn

# mydb = myconn.connect(host='localhost', user='root', password='9595946682', database='legion')

# db_cursor = mydb.cursor()

# db_delete = 'DELETE FROM family WHERE f_name=%s'
# db_value = ('sejal',)  # Note the comma to make it a tuple

# db_cursor.execute(db_delete, db_value)
# mydb.commit()

# print(db_cursor.rowcount, "row deleted")
