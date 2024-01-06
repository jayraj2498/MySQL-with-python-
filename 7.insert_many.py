
import mysql.connector as myconn

mydb = myconn.connect(user='root', host='localhost', password='9595946682', database='legion')

db_cursor = mydb.cursor()

db_insert = "INSERT INTO family (roll_no, f_name, l_name, age) VALUES (%s, %s, %s, %s)"
db_list = [(4, 'snehal', 'sonawane', 29),
           (5, 'akansh', 'jade', 21),
           (6, 'sejal', 'sonar', 20)]

db_cursor.executemany(db_insert, db_list)

mydb.commit()

print(db_cursor.rowcount, 'rows inserted')





# # another record 


# import mysql.connector as myconn

# mydb = myconn.connect(user='root', host='localhost', password='9595946682', database='legion')

# db_cursor = mydb.cursor() 

# db_insert= 'insert into cricket(jersy_no, f_name, l_name, age, runs) values(%s,%s,%s,%s,%s) ' 

# db_list=[(10, 'Virat', 'Kohli', 32, 12000),
#         (7, 'Rohit', 'Sharma', 34, 9200),
#         (18, 'Steve', 'Smith', 31, 8000),
#         (45, 'Kane', 'Williamson', 30, 6500),
#         (3, 'Joe', 'Root', 29, 7500)]

# db_cursor.executemany(db_insert , db_list ) 

# mydb.commit()

# print(db_cursor.rowcount , 'row inserte') 





