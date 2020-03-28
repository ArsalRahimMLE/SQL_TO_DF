# Imports #
import sqlalchemy
import os, fnmatch
import pandas as pd

class sqlCred:
    def __init__(self,
                database: str,
                host: str = '127.0.0.1',
                username : str = 'SA',
                password :str = 'abc$12345',
                OS:str='Linux',

                ):
        """
        :param database: Specify the name of the database from which you want to fetch the data
        :param host (optional): By default it is localhost (127.0.0.1) but in case of remote database you can replace the IP of the server #
        :param username: Database user name
        :param password: Password for database username
        :param OS (Optional): By default it is 'linux' but in case of windows specify 'Windows'
        """
        # Set values to local variables #
        if not database:
            pass # Need to add raise exception later #
        self.database = database
        if username and password:
            self.username = username
            self.password = password
        self.host = host
        # if OS is linux #
        if OS == 'Linux':
            self.driver = find_driver_linux('libmsodbcsql*', '/opt/')
            # create a connection string #
            self.conn = 'mssql+pyodbc://'+self.username+':'+self.password+'@'+self.host+'/'+self.database+'?driver='+self.driver
        # else windows #
        else:
            self.conn = 'mssql+pyodbc://' + self.username + ':' + self.password + '@' + self.host + '/' + self.database + '?driver=' + self.driver


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
    # 04 close the connection #
    #connection.close()
    # 05 return the dataframe #
    return dt


def to_sql(credentials:sqlCred, dataframe:pd.DataFrame, table_name:str):
    # 01 fetch the connection string from the sqlCred class #
    conn = credentials.conn
    # 02 establish connection using connection string #
    connection = establish_connection(conn)
    # 03 store data to the database #
    dataframe.to_sql(name=table_name, con=connection)
    # 04 close the connection #
    #connection.close()

def find_driver_linux(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result[0]