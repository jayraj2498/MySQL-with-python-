import mysql.connector as my_conn

my_db = my_conn.connect(
    host="localhost",
    user="root",
    password="9595946682")

print(my_db, "connected")
