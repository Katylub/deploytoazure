import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg

class ClientDao:
    
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['username'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )

    """def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = '',
            database ='datarepresentationfinal'
        )
    
        #print ("connection made")"""

    def create(self, client):
        cursor = self.db.cursor()
        sql = "insert into clients (Names, Surname, Price) values (%s,%s,%s)"
        values = [
            
            client['Names'],
            client['Surname'],
            client['Price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from clients'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, ClientID):
        cursor = self.db.cursor()
        sql = 'select * from clients where ClientID = %s'
        values = [ ClientID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, client):
       cursor = self.db.cursor()
       sql = "update clients set Names = %s, Surname = %s, Price = %s where ClientID = %s"
       values = [
           client['Names'],
           client['Surname'],
           client['Price'],
           client['ClientID']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return client

    def delete(self, ClientID):
       cursor = self.db.cursor()
       sql = 'delete from clients where ClientID = %s'
       values = [ClientID]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['ClientID','Names', 'Surname', 'Price']
        client = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                client[colName] = value
        return client

clientDao = ClientDao()