import mysql.connector
from mysql.connector import Error

# Create a connection
'''maybe put in parameters'''
def createConnection(dbName):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='pacer_bot',#switch out?
                                             user='root',
                                             password='root')
        return connection
    except mysql.connector.Error as error:
        print(error)

# Should only be called once per server
def createRunnersTable(serverID):
    try:
        connection = createConnection('pacer_bot')
        createTable = """CREATE TABLE DB_""" + str(serverID) + """(
                                   User varchar(250) NOT NULL,
                                   RunDate datetime NOT NULL,
                                   Distance DECIMAL(10,2) NOT NULL,
                                   Time int NOT NULL,
                                   Primary Key (User, RunDate))"""

        cursor = connection.cursor()
        result = cursor.execute(createTable)
        print("Guild (" + str(serverID) + ") Table created successfully")
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

# return true if a table exists false if it doesn't
def tableExists(tableName):
    tableName = "DB_" + str(tableName)
    connection = createConnection('tableName')
    cursor = connection.cursor()
    select_stmt = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = %(tableName)s"
    cursor.execute(select_stmt, {'tableName' : tableName})
    print("yuh")
    if cursor.fetchone()[0] == 1:
        cursor.close()
        connection.close()
        return True
    connection.close()
    cursor.close()
    return False

def insertInfo(user, ):
    pass