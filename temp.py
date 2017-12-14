import matplotlib.pyplot as plt
import csv
import numpy as np
import urllib
import matplotlib.dates as mdates
import datetime
import pandas as pd


url = "http://chartapi.finance.yahoo.com/instrument/1.0/GOOG/chartdata;type=quote;range=5y/csv"
source_code = urllib.request.urlopen(url).read().decode()

# No need in new version of matplotlib
def bytespdate2num(fmt, encoding='utf-8'):
	strconverter = mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s = b.decode(encoding)
		return strconverter(s)
	return bytesconverter

# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1), (0,0))

# for xlabel in ax1.get_xticklabels():
# 	xlabel.set_rotation(45)


stock_data = []
split_source = source_code.split('\n')

for line in split_source:
	split_line = line.split(',')
	# print(split_line)
	if len(split_line) == 6:
		if 'values' not in line:
			stock_data.append(line)


date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y%m%d')})

plt.plot_date(date, closep, '-')
plt.show()

# df = pd.DataFrame(stock_data, dtype=float)
# a = 0

# for i in df[0]:
# 	df.ix[a,0] = datetime.datetime.fromtimestamp(i)
# 	a+=1

# print(df.head())
# print(df.ix[0])

# stock = []
# for i in range(len(df)):
# 	stock.append(df.ix[i])

# print(stock[0:10])

# date = df[0]
# # print(date[0:10])

# close = df[1]
# print(close[0:10])

# ax1.plot_date(date, close, '-', label="Stock")
# ax1.grid(True, color='b')
# plt.subplots_adjust(left=0.12, bottom=0.20, right=0.90, top=0.90, wspace=0.2, hspace=0.2)
													  							 

# plt.plot(date, closep, label="Price")