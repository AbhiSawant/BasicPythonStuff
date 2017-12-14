import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import csv
import numpy as np
import urllib
import datetime
import pandas as pd


comp_stock = 'EBAY'
# x = [1, 2, 3]
# y = [4, 5, 6]

# x2 = [1 ,2, 3]
# y2 = [10, 14, 18]


# plt.plot(x, y, label="First Line")
# plt.plot(x2, y2, label="Second Line")


#################################################################
#Getting data from internet

url = "http://chartapi.finance.yahoo.com/instrument/1.0/"+comp_stock+"/chartdata;type=quote;range=1m/csv"
source_code = urllib.request.urlopen(url).read().decode()

def bytespdate2num(fmt, encoding='utf-8'):
	strconverter = mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s = b.decode(encoding)
		return strconverter(s)
	return bytesconverter

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

for xlabel in ax1.get_xticklabels():
	xlabel.set_rotation(45)


stock_data = []
split_source = source_code.split('\n')

for line in split_source:
	split_line = line.split(',')
	# print(split_line)
	if len(split_line) == 6:
		if 'values' not in line:
			stock_data.append(line)


date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y%m%d')})

x = 0
y = len(date)
ohlc = []

while x < y:
	append = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
	ohlc.append(append)
	x+=1

candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))

plt.subplots_adjust(left=0.12, bottom=0.24, right=0.90, top=0.90, wspace=0.2, hspace=0.2)


# ax1.grid(True, color='y', linestyle='-', linewidth=0.5) #color=’r’, linestyle=’-‘, linewidth=2
# plt.subplots_adjust(left=0.12, bottom=0.20, right=0.90, top=0.90, wspace=0.2, hspace=0.2)
# ax1.xaxis.label.set_color('#5aec11')
# ax1.yaxis.label.set_color('#5aec11')
# ax1.set_yticks([15, 20, 25, 30, 35])
# ax1.plot_date(date, closep, '-', label="EBAY", color='Black')
# ax1.plot([], [], linewidth=5, label='Gain', color='g', alpha=0.5)
# ax1.plot([], [], linewidth=5, label='Loss', color='r', alpha=0.5)
# ax1.axhline(22, linewidth=5, color='#5aec11')
# ax1.fill_between(date, closep, 22, where=closep>22, facecolor='g',alpha=0.5)
# ax1.fill_between(date, closep, 22, where=closep<22, facecolor='r',alpha=0.5)

# ax1.spines['left'].set_color('b')
# ax1.spines['top'].set_visible(False)
# ax1.spines['right'].set_visible(False)
# ax1.spines['left'].set_linewidth(5)

# ax1.tick_params(axis='x', colors='b')


####################################
#Getting data from internet using UXIX time

# url = "http://chartapi.finance.yahoo.com/instrument/1.0/GOOG/chartdata;type=quote;range=10d/csv"
# source_code = urllib.request.urlopen(url).read().decode()

# # No need in new version of matplotlib
# # def bytespdate2num(fmt, encoding='utf-8'):
# # 	strconverter = mdates.strpdate2num(fmt)
# # 	def bytesconverter(b):
# # 		s = b.decode(encoding)
# # 		return strconverter(s)
# # 	return bytesconverter

# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1), (0,0))

# for xlabel in ax1.get_xticklabels():
# 	xlabel.set_rotation(45)


# stock_data = []
# split_source = source_code.split('\n')

# for line in split_source:
# 	split_line = line.split(',')
# 	# print(split_line)
# 	if len(split_line) == 6:
# 		if 'values' not in line:
# 			stock_data.append(pd.Series(split_line))

# df = pd.DataFrame(stock_data, dtype=float)
# a = 0

# for i in df[0]:
# 	df.ix[a,0] = datetime.datetime.fromtimestamp(i)
# 	a+=1



# # print(df.head())
# # print(df.ix[0])

# # stock = []
# # for i in range(len(df)):
# # 	stock.append(df.ix[i])

# # print(stock[0:10])

# date = df[0]
# # print(date[0:10])

# close = df[1]
# # print(close[0:10])

# # Or use vectorize method
# datatodate = np.vectorize(datetime.datetime.fromtimestamp)
# date = datatodate(date)

# ax1.plot_date(date, close, '-', label="Stock")
# ax1.grid(True, color='b')
# plt.subplots_adjust(left=0.12, bottom=0.20, right=0.90, top=0.90, wspace=0.2, hspace=0.2)
													  							 

# # plt.plot(date, closep, label="Price")


####################################
#Loading data from files
 
#Using CSV
# x = []
# y = []

# with open('eg.csv', 'r') as csvfile:
# 	plot = csv.reader(csvfile, delimiter=',')
# 	for rows in plot:
# 		# print(rows)
# 		x.append(int(rows[0]))
# 		y.append(int(rows[1]))

#Using Numpy

# x, y = np.loadtxt('eg.csv', delimiter=',', unpack=True)

# plt.plot(x, y, label='Loaded from file')



#####################################
#Pie Chart
#matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, 
#autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, 
#startangle=None, radius=None, counterclock=True, wedgeprops=None, 
#textprops=None, center=(0, 0), frame=False, hold=None, data=None)

# slices = [7, 2, 9, 6]
# act = ['Sleeping', 'Eating', 'Working', 'Playing']
# color = ['Red', 'Yellow', 'Green', 'Blue']
# plt.pie(slices, labels=act, 
# 		colors=color, autopct='%1.1f%%', shadow=True,
# 		explode=(0,0.2,0,0))



######################################
#Stack Plots

# matplotlib.pyplot.stackplot(x, *args, **kwargs)
# days = [1,2,3,4,5]

# sleeping = [7,8,6,11,7]
# eating   = [2,3,4,3,2]
# working  = [7,8,7,2,2]
# playing  = [8,5,7,8,13]

# plt.stackplot(days, sleeping,eating,working,playing, labels=['Sleeping', 'Eating', 'Working', 'Playing'], colors=['r','y','b','g'])

#######################################
#Scatter Plots

#matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, 
#cmap=None, norm=None, vmin=None, vmax=None, alpha=None, 
#linewidths=None, verts=None, edgecolors=None, hold=None, data=None, **kwargs

# x = [1,2,3,4,5,6,7,8]
# y = [2,5,1,8,9,3,1,8]

# plt.scatter(x, y, label='Scatter', color='Blue', marker='X', s=100)


########################################
#Histograms

#matplotlib.pyplot.hist(x, bins=None, range=None, normed=False, weights=None, 
#cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', 
#rwidth=None, log=False, color=None, label=None, 
#stacked=False, hold=None, data=None, **kwargs)


# pop_ages = [10,51,48,75,98,100,120,109,48,26,12,20,35,9,48,85,95,35,71,73,94,72,81,49,59,38,71,35]
# # ids = [x for x in range(len(pop_ages))]
# # plt.bar(ids, pop_ages)
# bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]

# plt.hist(pop_ages, bins, histtype='bar', rwidth=0.8, align='left')


#########################################
#Bar Charts

# x = [2, 4 ,6, 8, 10]
# y = [5, 8, 7 ,3 ,9]

# x2 = [1, 3, 5, 7, 9,11]
# y2 = [5, 8, 9, 1, 4, 7]

# plt.bar(x, y, label="Bars1", color='Yellow')
# plt.bar(x2, y2, label="Bars2", color='Blue')

##########################################
#Labels  and legends:

# plt.plot(x, y, label="First")
# plt.plot(x1, x2, label='Second')



plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Stocks")
plt.legend()
plt.show()