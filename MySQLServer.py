import mysql.connector 


try:
    with mysql.connector.connect(
        host="localhost",
        user="",
        password=""   
    ) as connection:
        query = "CREATE DATABASE IF NOT EXISTS alx_book_store;"

        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(e)
