import numpy as np
import pandas as pd
import sklearn


#Many-to-one
df1 = pd.DataFrame({"Key":['b', 'b', 'a', 'c', 'a', 'a', 'b'], "Data1": range(7)})

df2 = pd.DataFrame({"Key":['a', 'b', 'd'], "Data2":range(3)})

print(pd.merge(df1, df2, on="Key", sort=True))
#Options available
#DataFrame.merge(right, how='inner', on=None, \
#left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False)

#With different key values
df3 = pd.DataFrame({"LKey":['a', 'b', 'a', 'c', 'a', 'a', 'b'], "Data1": range(7)})

df4 = pd.DataFrame({"RKey":['a', 'b', 'd'], "Data2":range(3)})

print(pd.merge(df3, df4, left_on="LKey", right_on="RKey"))

print(pd.merge(df1, df2, how="outer"))

#Many to many
df5 = pd.DataFrame({"Key":['b', 'b', 'a', 'c', 'a', 'b'], "Data1": range(6)})

df6 = pd.DataFrame({"Key":['a', 'b', 'a', 'b','d'], "Data2": range(5)})

print(pd.merge(df5, df6, on="Key"))

print(pd.merge(df5, df6, on="Key", how="left"))

#Based of more than key

left = pd.DataFrame({"City":["Mumbai", "Mumbai", "Pune"], 
					 "Loc":["Andheri", "Malad", "Kothrud"],
					 "MPopulation":[510000, 245411, 187444]})

right = pd.DataFrame({"City":["Mumbai", "Mumbai", "Pune", "Pune"], "Loc":["Andheri", "Goregaun", "Kothrud", "Pimpri"], 
						"FPopulation":[364000, 2571571, 267444, 138518]}, columns=["City", "Loc", "FPopulation"])


print(pd.merge(left, right, on=["City", "Loc"]))

print(pd.merge(left, right, on=["City", "Loc"], how="outer"))

print(pd.merge(left, right, on="City"))

print(pd.merge(left, right, on="City", suffixes=("_left", "_right")))

#Merging on index

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})

right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

print(pd.merge(left1, right1, left_on="key", right_index=True))
print(pd.merge(left1, right1, left_on="key",left_index=True, right_index=True))#returns empty df
print(pd.merge(left1, right1, left_on="key", right_index=True, how="outer"))

#Hierarchical indexing

lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'key2': [2000, 2001, 2002, 2001, 2002], 'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)), index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
						[2001, 2000, 2000, 2000, 2001, 2002]], columns=['event1', 'event2']) 

print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how="outer"))
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how="outer", sort=True))#sort default false

left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'], columns=['Ohio', 'Nevada'])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]], index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])

print(pd.merge(left2, right2, how='outer', left_index=True, right_index=True))

print(left2.join(right2, how='outer'))

another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]], index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])

print(left2.join([right2, another]))

#Concatenating Along an Axis

arr = np.arange(12).reshape((3,4))
print(np.concatenate([arr, arr], axis=0))
print(np.concatenate([arr, arr], axis=1))


s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

print(pd.concat([s1, s2]))
print(pd.concat([s1, s2, s3], axis=1))

s4 = pd.concat([s1 * 5, s3])
print(pd.concat([s1, s4], axis=1))
print(pd.concat([s1, s4], axis=1, join='inner'))
pd.concat([s1, s4], axis=1, join='inner', join_axes=[['a', 'b', 'c', 'e']])
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
print(result.unstack())
result = pd.concat([s1, s2, s3], keys=['one', 'two', 'three'], axis=1)
print(result)
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'], columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'], columns=['three', 'four'])
print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], axis=1))
print(pd.concat([df1, df2], axis=1, keys=['One', 'Two']))#Hierarchical indexing
print(pd.concat([df1, df2], axis=1, keys=['Level_1', 'Level_2'], names=['Upper', 'Lower']))
print(pd.concat([df1, df2]))
print(pd.merge(df1, df2, left_index=True, right_index=True))

#Reshaping and pivoting

data = pd.DataFrame(np.arange(6).reshape((2,3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='State'),
                    columns=pd.Index(['one', 'two', 'three'], name='Number'))

print(data)
result = data.stack()
result
result.unstack()
result.unstack(0)
result.unstack('Number')
result.unstack('State')
s1 = pd.Series([1, 2, 3, 4],index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
s1
s2
data2 = pd.concat([s1,s2], keys=['one', 'two'])
data2
data2.unstack()
data2.unstack().stack()
data2.unstack().stack(dropna=False)
result
df = pd.DataFrame({'Left':result, 'Right':result + 5},
                  columns=pd.Index(['Left', 'Right'], name='Side'))
 df
 df.unstack('State')
 df.unstack('State').stack('Side')
 
