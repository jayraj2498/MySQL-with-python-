import mysql.connector as myconn

mydb = myconn.connect(user='root', host='localhost', password='9595946682', database='legion')

db_cursor = mydb.cursor() 

db_update="update family  set age=%s  where roll_no=%s "
db_value=(23,3)
db_cursor.execute(db_update,db_value) 
mydb.commit()

print(db_cursor.rowcount ,"value inserted ")





# import mysql.connector as myconn

# mydb = myconn.connect(user='root', host='localhost', password='9595946682', database='legion')

# db_cursor = mydb.cursor()

# # Update statement
# db_update = "UPDATE family SET age=%s WHERE roll_no=%s"
# db_values = (23, 3)

# # Execute the update
# db_cursor.execute(db_update, db_values)

# # Check for errors
# if db_cursor.rowcount > 0:
#     print(f"{db_cursor.rowcount} row(s) updated.")
# else:
#     print("No rows updated. Check if the row with roll_no=3 exists.")






