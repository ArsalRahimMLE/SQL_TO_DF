from bcpandas import sqlCred, read_sql, to_sql

if __name__=="__main__":
    creds = sqlCred('my_server','my_db','my_username','my_password')
  