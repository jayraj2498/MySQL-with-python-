# insert data into family table 

# import mysql.connector as myconn 
# mydb=myconn.connect(user='root',host='localhost',password='9595946682',database='legion') 

# db_cursor=mydb.cursor()

# insert_db="insert into family(roll_no, f_name, l_name, age) values(%s,%s,%s,%s) "
# db_value=[(7,'sanket','nagre',25),
#           (8,'suraj','nagre',25),
#           (9,'ashirwad','dhongade',25)]

# db_cursor.executemany(insert_db,db_value) 

# mydb.commit() 

# print(db_cursor.rowcount ,"row inserted") 



# fetch all rrrecord from family table 

# import mysql.connector as myconn 
# mydb=myconn.connect(user='root',host='localhost',password='9595946682',database='legion') 

# db_cursor=mydb.cursor() 

# db_cursor.execute('select * from family') 

# for record in db_cursor.fetchall():
#     print(record)