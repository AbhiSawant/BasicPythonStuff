import pandas as pd
import pyodbc

con = pyodbc.connect("DRIVER={SQL Server}; server=ABHISHEK\SQLEXPRESSABHI; database=AdventureWorks2012; Trusted_connection=yes")
#Trusted_connection=yes tells its a windows authentication
cur = con.cursor()
#SQL queries
sql = "select * from HumanResources.Department"

cur.execute(sql)
for row in cur:
	print(row[0], row[1], row[2], row[3])


 #####################################################################
 #					Storing DB info in pandas df			 	     #		
 #####################################################################


df = pd.read_sql(sql, con)
print(df.head())

cur.close()
con.close()