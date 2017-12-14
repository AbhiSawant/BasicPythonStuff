import pandas as pd
import sys
import numpy as np
import csv
import urllib
from lxml.html import parse
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

# df = pd.read_csv('Names.csv', header=None, names=['A', 'B'])
# df = pd.read_csv('Names.csv', skiprows=[1], index_col='Sr.No', na_values=['NULL', 23])
# df = pd.read_csv('Names.csv', skiprows=[1], nrows=4)


#Dividing data in chunks(in this eg chunks of 2)
# df = pd.read_csv('Names.csv', skiprows=[1], chunksize=2)

# for i in df:
# 	print(i)


# print(tot)
#Checking boolean
# print(pd.isnull(df))
# print(pd.read_table('train.csv', sep=','))


#Reading file seperated by muliple spaces
# txt = pd.read_csv('test.txt', sep='\s+')
# print(txt)


#Reading using read_table default sep is tab
# txt2 = pd.read_table('test.txt', sep='\t')
# print(txt2)

# txt3 = pd.read_table('test.txt', sep='\s+')
# print(txt3)


#Writing data out
# df = pd.read_csv('Names.csv', skiprows=[1])
# print(df)

# df.to_csv(sys.stdout, cols=['Names'], sep='-', index=False)


#Series to_csv format
# ser = pd.Series(np.arange(10))
# print(ser)

# ser.to_csv(sys.stdout)


#Working with discrepancies in file
# f = open('Names.csv')
# reader = csv.reader(f)

# for line in reader:
# 	print(line)

# f.close()
# # When there are discrepancies in the file read_csv gives an error
# f1 = pd.read_csv('Names.csv')
# print(f1)


# print()
# print()
# class MyDialect(csv.Dialect):
# 	delimiter = "|"
# 	doublequote = False
# 	lineterminator = '\n'
# 	quotechar = "'"
# 	quoting = csv.QUOTE_MINIMAL

# with open("writecsv.csv", 'w') as fw:
# 	writer = csv.writer(fw, delimiter="#", lineterminator='\n', quoting = csv.QUOTE_NONE, quotechar = "'")
# 	writer.writerow(('FName', 'LName'))
# 	writer.writerow(('Abhi', 'Sawant'))
# 	writer.writerow(("Neha", "Rane"))
	
# f10 = open("writecsv.csv")

# r10 = csv.reader(f10)
# for l in r10:
# 	print(l)
# f10.close()
# print()
# print()
# f11 = open("writecsv.csv")
# print(f11.read())

 #####################################################################
 #					WebScraping using usllib						 #
 #####################################################################


# parsed = parse(urlopen("http://www.mumbaiyellowpages.org/"))
# doc = parsed.getroot()
# print(doc)
# links = doc.findall('.//a')
# # print(links)
# # reflink = links[2].get('href')
# # print(reflink)

# #Print all the links available in specified node
# # for i in range(len(links)):
# #     temp = links[i].get('href')
# #     print(temp)

# #Indntifing tables 
# tables = doc.findall(".//table")



# print("Table:\n")
# print(tables)
# rows1 = tables[4].findall(".//tr")
# print("Rows:\n")
# print(rows1)
# print("Ele\n")
# ele = rows1[0].findall('.//td')
# print(ele)
# print(len(ele))
# print(ele[0].text_content())

#Above thing in loop
# for ti in range(len(tables)):
# 	valr = tables[ti].findall(".//tr")
# 	for ri in range(len(valr)):
# 		vald = valr[ri].findall(".//td")
# 		for ei in range(len(vald)):
# 			try:
# 				print("Values in ele ", ei)
# 				print(vald[ei].text_content())

# 			except UnicodeEncodeError as u:
# 				print("Error", u)
# 				continue


 #####################################################################
 #					WebScraping using requests						 #
 #####################################################################
# WebScraping using Requests
# url = "https://www.youtube.com/results?search_query=web+scraping+python"
# r = requests.get(url) 
# print(r.content)
# print()
# print()

# try:
# soup = BeautifulSoup(r.content)	
# print(soup.prettify())
# except UnicodeEncodeError as u:
# 	print("Error",u)

# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()

# links = soup.find_all("a")
# print(soup.find_all("a"))

# for link in links:
# 	if "https" in link.get('href'):
# 		print("<a href=", link.get('href'), ">", link.text, "</a>")
	# print(link.text)
	# print(link.get('href'))	
	


 #####################################################################
 #			Finding links and info from tables from a site			 #
 #####################################################################

#  import urllib
#  from lxml.html import parse
#  from urllib import urlopen

#  url = "url_name"
#  parsed = parse(urlopen(url))
#  root = parsed.getroot()
#  links = root.findall(".//a")
#  for link in links:
#  	print("<a href=", link.get("href"), ">", link.text, "</a href")

#  tables = root.findall(".//table")
#  print(tables)#list of table eles
#  i = 0
# rows = table[i].findall(".//tr")
# print(rows)#list of row eles
# j = 0
# data = rows[j].finall(".//td")
# print(data)#list of data eles in that row
# print(data[0].text_content())#prints info in that particular data cell


 #####################################################################
 #				 Connecting python to SQL database			 	     #		
 #####################################################################

import pyodbc

con = pyodbc.connect("DRIVER = {SQL Server}; server = ABHISHEK\SQLEXPRESSABHI; database = AdventureWorks2012; Trusted_connection=yes")
cur = con.cursor()
cur.execute("select * from HumanResources.Department")
for row in con:
	print(row[0], row[1], row[2], row[3])

cur.close()
con.close()


 #####################################################################
 #				         SQL data to pandas		             	     #		
 #####################################################################


import pyodbc

con = pyodbc.connect("DRIVER = {SQL Server}; server = ABHISHEK\SQLEXPRESSABHI; database = AdventureWorks2012; Trusted_connection=yes")

sql = "select * from HumanResources.Department"

df = pd.read_sql(sql, con)
print(df.head())

