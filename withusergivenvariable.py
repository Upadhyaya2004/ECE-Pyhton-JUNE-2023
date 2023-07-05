import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="msit"
)
mycursor=mydb.cursor()
 
sql="INSERT INTO customers(name, address) VALUES(%s,%s)"
a=str(input("Enter your name -> "))
b=str(input("Enter your address -> "))
val=(a , b)
mycursor.execute(sql,val)
sql_2="INSERT INTO customers_students(name, address,email,gender) VALUES(%s,%s,%s,%s)"
a=str(input("Enter your name -> "))
b=str(input("Enter your address -> "))
c=str(input("Enter your email -> "))
d=str(input("Enter your gender -> "))
val_2=(a,b,c,d)
mycursor.execute(sql_2,val_2)
mydb.commit()
print(mycursor.rowcount,"record inserted")
