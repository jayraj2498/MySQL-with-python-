import mysql.connector as myconn

mydb=myconn.connect(user='root', host='localhost', password='9595946682', database= 'legion') 

db_cursor=mydb.cursor()
db_cursor.execute('create table cricket  (jersy_no int primary key , f_name varchar(10) , l_name varchar(10)  , age int ,runs int) ') 

print("your table is created ") 



# import mysql.connector as myconn

# mydb = myconn.connect(user='root', host='localhost', password='9595946682', database='legion')

# db_cursor = mydb.cursor()
# # Corrected SQL query with a comma between f_name and l_name, and a closing parenthesis
# db_cursor.execute('CREATE TABLE family (roll_no INT PRIMARY KEY, f_name VARCHAR(10), l_name VARCHAR(10), age INT)')

# print("Your table is created")
