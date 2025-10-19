import mysql.connector


# try:
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!kabi@root104274eR$?"   
)

db_cursor = db.cursor()

sql = "CREATE DATABASE IF NOT EXISTS alx_book_store;"
db_cursor.execute(sql)
db.commit()

print("Database 'alx_book_store' created successfully!")

