# importing the mysql module so we can connnect to mysql

import mysql.connector


#I think itll be good to have the database as its own class
#db class to be exported to main app
class DB:
    # methods
    def initdb(self):
        mydb = mysql.connector.connect(
            host="35.239.196.216",
            user="root",
            password="dad"
            )
        print(mydb)
        print("connection successful!")
        # cursor = mydb.cursor()

