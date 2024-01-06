import mysql.connector as myconn

mydb=myconn.connect(user='root', host='localhost', password='9595946682', database= 'legion') 

db_cursor=mydb.cursor()
db_cursor.execute('insert into cricket(jersy_no, f_name, l_name, age, runs) values(%s,%s,%s,%s,%s) ',
                  (7,'MS','Dhoni',38,10000) ) 

mydb.commit()
print(db_cursor.rowcount  , "record_inserted")







db_cursor=mydb.cursor() 
db_cursor.execute("insert into family(roll_no,f_name,l_name,age) values(%s,%s,%s,%s)"  ,
                  (1,'jayraj','sonawae',25)) 

mydb.commit()
print(db_cursor.rowcount  , "record_inserted")





 

import mysql.connector as myconn

mydb = myconn.connect(user='root', host='localhost', password='9595946682', database='legion')

db_cursor = mydb.cursor()

# Corrected tuple syntax
db_cursor.execute("INSERT INTO family (roll_no, f_name, l_name, age) VALUES (%s, %s, %s, %s)",
                  (2, 'aksh', 'jade', 24),
                  )

mydb.commit()
print(db_cursor.rowcount, "records inserted")  
