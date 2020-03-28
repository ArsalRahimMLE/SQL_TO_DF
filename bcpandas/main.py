# Imports #
import sqlalchemy
import pyodbc
import pandas as pd

class sqlCred:
    def __init__(self,
                database: str,
                host: str = '127.0.0.1',
                username : str = 'SA',
                password :str = 'abc$12345',
                driver: str = '/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.5.so.2.1'
                ):
        if not database:
            pass # Need to add raise exception later #
        self.database = database
        if username and password:
            self.username = username
            self.password = password
        self.driver = driver
        # create a connection string #
        self.conn = 'mssql+pyodbc://'+username+':'+password+'@'+host+'/'+database+'?driver='+driver
        #self.conn = 'mssql+pyodbc://SA:abc$12345@127.0.0.1/Northwind_Db?driver=/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.5.so.2.1'
        print('hello')

def establish_connection(connection_string):
    # 01 create connection using sqlalchemy #
    # need to add exception later on -- REMEMBER #
    connection = sqlalchemy.create_engine(connection_string)
    # 02 return the database end-point #
    return connection


def read_sql(credentials:sqlCred, table_name:str):
    # 01 fetch the connection string from the sqlCred class #
    conn = credentials.conn
    # 02 establish connection using connection string #
    connection = establish_connection(conn)
    # 03 fetch the data from the database #
    dt = pd.read_sql_query('SELECT * FROM '+table_name, connection)
    # 04 return the dataframe #
    return dt

def to_sql():
    print('to sql method')