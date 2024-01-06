import mysql.connector as myconn 

mydb=myconn.connect(host="localhost",user="root",password="9595946682") 

db_cursor=mydb.cursor() 
db_cursor.execute("create database legion") 

print("databse created succesfully")