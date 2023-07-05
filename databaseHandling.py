import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="msit"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers_students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255),email VARCHAR(100),gender TEXT(50))")
print("table created sucessfully")


