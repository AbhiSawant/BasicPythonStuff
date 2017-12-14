import pandas as pd

data = {'State':['Mumbai', 'Delhi', 'Banglore', 'Chennai'],
		'Pop':[3.5, 2.3, 1.2, 2.8],
		'Year':[2005, 2004, 2002, 2008]}

# print(data)

frame = pd.DataFrame(data, columns = ['Year', 'State', 'Pop'])
# print(frame)

frame1 = pd.DataFrame(data, columns = ['Year', 'State', 'Pop', 'Debt'])
# print(frame1)

frame2 = pd.DataFrame(data, columns = ['Year', 'State', 'Pop', 'Debt'], index = ['one', 'two', 'three', 'four'])
# print(frame2)

# val = pd.Series([-1.2, -1.5], index = ['two', 'three'])
# print(val)
val = pd.Series([-1.2, -1.5])
frame2['Debt'] = val
# print(frame2)

# frame2['Eastern'] = frame2.State == 'Mumbai'
# print(frame2)

# del frame2['Eastern']
# print(frame2.columns)

data2 = {'Mumbai':{2000:2.4, 2001: 2.5},
		 'Banglore':{2001:1.6, 2002:1.8}}

# frame3 = pd.DataFrame(data2, columns = ['Mumbai', 'Banglore'])
# print(frame3)
# print(frame3.T)
	
frame3 = pd.DataFrame(data2, columns = ['Mumbai', 'Banglore'], index = [2001, 2002, 2003])
frame3.index.name = 'Year'
frame3.columns.name = 'State'
print(frame3)
# print(frame3.values)

# print(frame3['Mumbai'][:3])
# pdata = {'Mumbai': frame3['Mumbai'][:-1],
# 		 'Banglore': frame3['Banglore'][:2]}

# frame4 = pd.DataFrame(pdata)
# print(frame4)

obj = pd.Series(range(3), index = ['a', 'b', 'c'])
index = obj.index
print(obj.index)
# index[1] = 'd'

# print(index.size)
# print(index.flags)
# print(index.dtype)
# print(index.shape)
# print(index.nbytes)

print(index.get_values())
print(index.is_boolean())
print(index.max())
print(index.summary('Year'))
print(index.holds_integer())


# print(obj.index is index)
# print('Mumbai' in frame3.columns)


		