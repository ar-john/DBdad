# importing the mysql module so we can connnect to mysql

import mysql.connector

# mysql module using the connector.connect to connect tothe mysql db
mydb = mysql.connector.connect(
    host="35.239.196.216",
    user="root",
    password="dad"

)
print(mydb)

cursor = mydb.cursor()

print("connection successful!")
# cursor.execute("USE car;
#     SELECT year, model 
#     WHERE make="Ford")

    