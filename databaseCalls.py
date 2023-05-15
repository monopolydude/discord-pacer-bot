import mysql.connector
from mysql.connector import Error

#Should only be called once per server
def createRunnersTable(serverID):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='pacer_bot',
                                             user='root',
                                             password='root')
        createTable = """CREATE TABLE DB_""" + str(serverID) + """(
                                   User varchar(250) NOT NULL,
                                   RunDate datetime NOT NULL,
                                   Distance DECIMAL(10,2) NOT NULL,
                                   Time int NOT NULL,
                                   Primary Key (User, RunDate))"""

        cursor = connection.cursor()
        result = cursor.execute(createTable)
        print("Guild (" + str(serverID) + ") Table created successfully")
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))