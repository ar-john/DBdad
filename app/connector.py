# importing the mysql module so we can connnect to mysql

import mysql.connector
# importing python hash library
import hashlib

import tkinter as tk
import PartFinder

#I think itll be good to have the database as its own class
#db class to be exported to main app
class DB:
    # methods
    
    # new init method for the db
    def __init__(self):
        self.con = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root"
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
        #this loop takes our queried password and checks it against the given input
        for x in result:
            passw = passw.encode('UTF-8')
            #check if the entered passwords hash is the same as the stored password hash   
            hashed = hashlib.sha256(passw).hexdigest()
            print(x)
            print(hashed.upper())
            if hashed.upper() == x:
                print("successfully logged in")
                
            else:
                print("incorrect password")
                # logic
                return False

        return True
    

    #this method is to search the part with the array returned to us from PARTFINDER
    def searchPart(self, arr):
        i = 0
        for x in arr:
            print(x)
        





    def __del__(self):
        self.cursor.close()
        self.con.close()


