#   Python responsories
import os, mariadb, sqlite3, pandas as pd

from dotenv import load_dotenv

#   Loading the environment variables
load_dotenv()


#   Selecting, Inserting or updates a table
class MariaDB():

    '''
            #   Author : @Krigjo25
            #   Date   :  12.01-23

            #   Connecting to a database in MariaDB

            #   Features:
                -   Select records,
                -   Count row records
                -   Drop/Create/Show a database
                -   Delete Records

    '''

    def __init__(self, database):

        self.database = database

        #   Initializing the database connection
        self.conn = mariadb.connect(
                                    host = os.getenv('H0ST'), 
                                    user = os.getenv('MASTER'), 
                                    port = int(os.getenv('PORT')), 
                                    password = os.getenv('PASSWORD'),
                                    database = self.database)

        #   Creating a cursor to execute the statements
        self.cur = self.conn.cursor()

        return print(f"Connected to {self.database} ! Using MariaDB")

    def Database(self, arg, db):
        return self.cur.execute(f" {arg} DATABASE {db};")

    def SelectTable (self, table, *column, ):

        #   Initializing SQL variables
        query = ""
        sqlData = []
        
        #   Select a table from the database

        #   Ensure the column is not used
        if bool(column) == False:
            query = f"SELECT * from {table};"

        #   Ensure the column is used
        elif bool(column) == True:

            for i in column : query += f"{i}"
            query = f"SELECT {query} FROM {table};"

        #  Execute the query.
        try :

            self.cur.execute(query)

        except Exception as e: print(e)
        #   Fetching the sql selection
        sql = self.cur.fetchall()

        #   Iterating through the sql list
        for i in sql:
            for j in i:

                if j != None:
                    sqlData.append(j)

        #   Clear Memory
        del sql, query, column

        return sqlData

    def SelectRow(self, table, value, *column):

        #   Initializing SQL data
        query = ""
        sqlData = []
        

        #   Ensure the column is not used
        if bool(column) == False: 
            query = f"SELECT * FROM {table} WHERE categories = \"{value}\";"

        #  Execute the query.
        self.cur.execute(query)

        #   Fetching the sql selection
        sql = self.cur.fetchall()

        for i in sql:
            for j in i:
                if j != None:
                    sqlData.append(j)

        #   Clear Memory
        del sql, query, column

        return sqlData

    def SelectColumn(self, table, where, value, *column):

        #   Initializing SQL variables
        arg = ""
        sqlData = []

        #   Iterating through the argument
        for i in column : 
            arg += f"{i}"

        query = f"SELECT {arg}FROM {table} WHERE {where} = \"{value}\";"

        #  Execute the query.
        try :

            self.cur.execute(query)

        except Exception as e: print(e)
        else:

            #   Fetching the sql selection
            sql = self.cur.fetchall()

            #   Iterating through the sql list
            for i in sql:
                for j in i:

                    if j != None:
                        sqlData.append(j)

        #   Clear Memories
        del sql, query, column
        del value, where, arg

        #   Returning the values in sqlData
        return sqlData

    def RowCount(self, query):

        #   Executes the query and retrieve the rows
        self.cur.execute(query)

        #   Fetch the cursor
        self.cur.fetchall()

        #   Counts the rows in the cursor
        return self.cur.rowcount

    #   Not working properly
    def newRecord(self, database, table, *dbcolumn):

        #   Initializing variables
        column = ""
        values = ""
        #   Database selection
        self.conn.database = database

        #   How to know if its a column or value?
        for i in dbcolumn: column +=f"{i},"

        #   Creating a query to be executed
        query = f'INSERT INTO {table} ({column}) VALUES ({values})'

        #   Executes the query 
        self.cur.execute(query)
        self.conn.commit()

        #   Clear some space
        del i

        del query
        del column
        del database
        del dbcolumn
        del dbvalues
        

        return

    def DelRecord(self, *query):

        #   Executes the query 
        self.cur.execute(f'DELETE FROM {query[0]} WHERE {query[1]} = {query[3]};')
        self.conn.commit()

        #   Clear Memory
        del query

        return
    
class SQLite():

    '''
            #   Author : @Krigjo25
            #   Date   : 13.07-24

            #   Connecting to a database in SQLite3

            #   Features:
                -   Select records,
    '''

    def __init__(self, database):

        """ Initializing the database connection """
        self.database = database

        #   Initializing the database connection
        self.con = sqlite3.connect(f"{self.database}")

        #   Creating a cursor to execute the statements
        self.cur = self.con.cursor()

        return

    def SelectRecord(self, table, *column): 
        """ Selecting the whole table by column"""

        #   Initializing a string variable
        columns = ""

        #   Ensure that there is no values in the variable
        if bool(column) == False:
            columns = f"*"

        else:

            for i in range(len(column)):

                #   Ensure that the given Element is not the last element
                if column[i] != column[-1]:
                    columns +=f"[{column[i]}], "

                else:
                    columns +=f"[{column[i]}]"

        query = f"SELECT {columns} FROM {table}"

        #   Ensure the query statement is valid
        sqlite3.complete_statement(query)

        #   Execute the query
        query = pd.read_sql_query(query, self.con)

        #   Closing the connections
        self.con.close()

        #   Clear Memory
        del column, columns, table
        return query