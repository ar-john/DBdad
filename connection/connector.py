# importing the mysql module so we can connnect to mysql
# I feel like i can import more than just the connector,,
# like the whole mysql module
import mysql.connector
# 
mydb = mysql.connector.connect(
    host="35.239.196.216",
    user="root",
    password="dad"

)