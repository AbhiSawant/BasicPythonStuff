import matplotlib.pyplot as plt
import csv
import numpy as np
import urllib
import matplotlib.dates as mdates
import datetime
import pandas as pd



url = "http://chartapi.finance.yahoo.com/instrument/1.0/GOOG/chartdata;type=quote;range=10d/csv"
source_code = urllib.request.urlopen(url).read().decode()

stock_data = []
split_source = source_code.split('\n')


for line in split_source:
	split_line = line.split(',')
	# print(split_line)
	if len(split_line) == 6:
		if 'values' not in line:
			stock_data.append(pd.Series(split_line))

		
# df = pd.DataFrame(stock_data, dtype=float, columns=['Timestamp','close','high','low','open','volume'])
df = pd.DataFrame(stock_data, dtype=float)
a = 0

for i in df[0]:
	df.ix[a,0] = datetime.datetime.fromtimestamp(i)
	a+=1


print(df.head())
print(df.dtypes)
# print(df[[0],[1]])
print(df.ix[1,0])

