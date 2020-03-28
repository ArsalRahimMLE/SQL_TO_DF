from bcpandas import sqlCred, read_sql, to_sql

if __name__=="__main__":
    creds = sqlCred(database='Northwind_Db',username='SA',password='abc$12345')
    dt = read_sql(creds, table_name='Customers')
    to_sql(creds,dt,table_name='testing')
    print(dt.iloc[2])