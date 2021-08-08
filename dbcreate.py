import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root@123",
 
 port=3306)

mycursor = mydb.cursor()
mycursor.execute("Create database ddblog1")
