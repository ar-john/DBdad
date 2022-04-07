# importing the mysql module so we can connnect to mysql

import mysql.connector
# importing python hash library
import hashlib


#I think itll be good to have the database as its own class
#db class to be exported to main app
class DB:
    # methods
    
    # new init method for the db
    def __init__(self):
        self.con = mysql.connector.connect(
            host="35.239.196.216",
            user="root",
            password="dad"
            )
        print(self.con)
        print("connection successful!")

        self.cursor = self.con.cursor()

        mycursor = self.cursor.execute('use DadsParts;')
        print('using dadsparts db')

    #method to verify a users login request
    def authLogin(self, user, passw):
        #sql query that checks password at the emp_id
        sql = ('select passwd from EMPLOYEE where EMP_ID = ' + user + ';')
        #cursor executes the query
        self.cursor.execute(sql)
        #get our returned string too a variable
        result = self.cursor.fetchone()
        for x in result:
            print(x)

        passw.encode()
        #check if the entered passwords hash is the same as the stored password hash
        hashed = hashlib.sha1(passw).hexdigest()
        if hashed == result:
            print("successfully logged in")
        else:
            print("incorrect password")

    def __del__(self):
        self.cursor.close()
        self.con.close()


