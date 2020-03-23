
# Imports #

class sqlCred:
    def __init__(self,
                database: str,
                table: str,
                host: str = '127.0.0.1',
                username : str = 'SA',
                password :str = 'abc$12345',
                ):
        if not database and not table:
            pass #raise exception
        self.database = database
        self.table = table
        if username and password:
            self.username = username
            self.password = password

        pass

def read_sql():
    print('read sql method')

def to_sql():
    print('to sql method')