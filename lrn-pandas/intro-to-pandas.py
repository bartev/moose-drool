from pandas import Series, DataFrame
import pandas as pd

obj = Series([4, 7, -5, 3])
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000} 
obj3 = Series(sdata)
obj3

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)


# Create df from equal length dicts
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)

# Select colnames when defining df
DataFrame(data, columns=['year', 'state', 'pop'])

# define column with no data
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])

# Create df from nexted dicts
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)

obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])

frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])

data = DataFrame(np.arange(16).reshape((4, 4)),
index=['Ohio', 'Colorado', 'Utah', 'New York'],
columns=['one', 'two', 'three', 'four'])

data = DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])

frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

f = lambda x: x.max()
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

def f(x): return Series([x.min(), x.max()], index=['min', 'max'])



data = DataFrame({'Qu1': [1, 3, 4, 3, 4], 
		'Qu2': [2, 3, 1, 2, 3],
		'Qu3': [1, 5, 2, 4, 4]})


data = Series(np.random.randn(10),
index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],[1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

frame = DataFrame({'a': range(7), 'b': range(7, 0, -1),
'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
'd': [0, 1, 2, 0, 1, 2, 3]})