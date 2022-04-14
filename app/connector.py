#!/usr/bin/python
# importing the mysql module so we can connnect to mysql


import mysql.connector
# importing python hash library
import hashlib

import tkinter as tk

import CreateNewEmployee
#I think itll be good to have the database as its own class
#db class to be exported to main app
#so far all db queries come through here
class DB:
    # methods
    
    # new init method for the db
    def __init__(self):
        self.con = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Robot1.a"
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

    #method checks for the admin level of the user
    def chkAdmin(self, user):
        sql = ('select admin from EMPLOYEE where EMP_ID = ' + user + ';')
        self.cursor.execute(sql)
        #get our returned string too a variable
        result = self.cursor.fetchall()
        result = list(sum(result, ()))
        print(result)
        for x in result:
            print(result)
            if x == 1:
                return True


    #this method is to search the part with the array returned to us from PARTFINDER
    def searchPart(self, arr):
        # i = 0
        # new = []
        sql = ('select P.PART_NUM from PART P join COMPATIBLE COM on P.COMP_ID=COM.COMP_ID join CAR C on C.COMP_ID=COM.COMP_ID where C.CAR_YEAR= ' + arr[0] +
        ' and C.MAKE= \'' + arr[1] + '\' and C.MODEL= \'' + arr[2] + '\' and P.PART_DESC = \'' + arr[4]  + '\';') 
        print(sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        sanitizedResult = list(sum(result, ()))
        print(sanitizedResult)
        return sanitizedResult
        print(result)

    def getPart(self, partNum):
        query = "select * from PART where PART_NUM = " + str(partNum)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        sanitizedResult = list(sum(result, ()))
        print(sanitizedResult)
        return sanitizedResult

    def getCustomer(self, id):
        query = 'select fName, lName from CUSTOMER where CUST_ID = ' + str(id)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        sanitizedResult = list(sum(result, ()))
        print(sanitizedResult)
        return sanitizedResult

    def getCustomerCar(self, id):
        query = 'select CAR_ID from customer where cust_id = ' + str(id)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        sanitizedResult = list(sum(result, ()))
        print(sanitizedResult)
        return sanitizedResult

    def getCar(self, carid):
        query = 'select * from car where car_id = ' + str(carid)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        sanitizedResult = list(sum(result, ()))
        print(sanitizedResult)
        return sanitizedResult

    def getInvoice(self, invnum):
        query = 'select * from INVOICE where INV_NUM =  + \'' + invnum + '\''
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        result = list(sum(result, ()))
        print(result)
        return result

    def addPartToInvoice(self, invnum, partnum, qty):
        query = 'update invoice set PART_NUM = \'' + str(partnum) + '\' , PARTQTY = \'' + str(qty) + '\' where INV_NUM = \'' + str(invnum) + '\''
        print(query)
        self.cursor.execute(query)
        self.con.commit()
        return

    def getCustomers(self):
        query = 'select lname from customer order by lname'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        result = list(sum(result, ()))
        print(result)
        return result

    def getCustomerNumByName(self, name):
        query = 'select CUST_ID from customer where lname = \'' + name + '\''
        print(query)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        result = list(sum(result, ()))
        print(result)
        return result
            
    #this will input a new employee in the database        
    def createEmp(self, empId, fname, lname, admin, passw):
        print(passw)
        # i = passw.encode('utf-8')
          
        # hashed = hashlib.sha256(i).hexdigest()
        a = '0'
        if admin == 1:
            a='1'
        

        sql = ('insert into EMPLOYEE values (\'' + empId + '\', \'' + fname + '\',\'' + lname +  '\',\'' + a +  '\',\'' + self.hashpass(passw) +  '\');' ) 
        print(sql)
        self.cursor.execute(sql)
        print('employee entered')
        # result = self.cursor.fetchall()

        # print(result)

    def createCustomer(self, fname, lname, car):
        query = 'insert into CUSTOMER (car_id, fName, lname) values ( \'' + str(car) + '\', \'' + str(fname) + '\' , \'' + str(lname) + '\' );'
        print(query)
        self.cursor.execute(query)
        self.con.commit()
        return

    def getCarYears(self):
        query = 'select CAR_YEAR from CAR GROUP BY CAR_YEAR'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        sanitizedResult = list(sum(result, ()))
        print(sanitizedResult)
        return sanitizedResult

    def getMakesByYear(self, year):
        query = 'select MAKE FROM CAR WHERE CAR_YEAR = ' + year + ' GROUP BY MAKE'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        sanitizedResult = list(sum(result, ()))
        print(sanitizedResult)
        return sanitizedResult

    def getModelsByMake(self, make):
        query = 'select MODEL from CAR where MAKE = \'' + make + '\' GROUP BY MODEL'
        print(query)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        sanitizedResult = list(sum(result, ()))
        print(sanitizedResult)
        return sanitizedResult

    def getPartCategories(self, comp= None):
        query = 'select CATEGORY from PART WHERE COMP_ID = ' + str(comp) + ' GROUP BY CATEGORY'
        print(query)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        sanitizedResult = list(sum(result, ()))
        print(sanitizedResult)
        return sanitizedResult

    def getPartDescriptions(self, cat, comp = None):
        query = 'select PART_DESC from PART where CATEGORY = \'' + cat + '\' and  COMP_ID = ' + str(comp) + ' order by PART_DESC'
        print(query)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        sanitizedResult = list(sum(result, ()))
        print(sanitizedResult)
        return sanitizedResult

    def getCompatibility(self, year = None, make = None, model = None):
        query = 'SELECT COMP_ID FROM CAR WHERE CAR_YEAR = \'' + str(year) + '\' and  MAKE = \'' + make + '\' and MODEL = \'' + model + '\''
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        result = list(sum(result, ()))
        print(result)
        return result

    def getCarByYMM(self, year = None, make = None, model = None):
        query = 'SELECT CAR_ID FROM CAR WHERE CAR_YEAR = \'' + str(year) + '\' and  MAKE = \'' + str(make) + '\' and MODEL = \'' + str(model) + '\''
        print(query)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        result = list(sum(result, ()))
        print(result)
        return result[0]


    def addInvoiceToDB(self, invnum, custid, empid):
        query = 'insert into INVOICE (INV_NUM, CUST_ID, EMP_ID) values (\'' + invnum + '\', \'' + str(custid[0]) + '\',\'' + empid +  '\');'
        print(query)
        self.cursor.execute(query)
        self.con.commit()
        return

    def hashpass(self, passw):
        for x in passw:

            # i = x.encode('utf-8')
          
            hashed = hashlib.sha256(x.encode('utf-8')).hexdigest()

        return hashed

    



    def exit(self):
        self.cursor.close()
        self.con.close()
        print('db connection closed')

    def __del__(self):
        self.cursor.close()
        self.con.close()
        print('db connection closed')


