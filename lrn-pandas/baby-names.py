import pandas as pd
import numpy as np

names1880 = pd.read_csv('pydata-book/ch02/names/yob1880.txt', names=['name', 'sex', 'births'])
names1880[:10
]
# count num births by gender
names1880.groupby('sex').births.sum()

# Download from a group of files
years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'pydata-book/ch02/names/yob%d.txt'  % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

# Concatenate everything into a single df
# ignore_index=True because not interested in original row numbers from read_csv
names = pd.concat(pieces, ignore_index=True)

total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum)
total_births.plot(title='Total births by sex and year')

# This function is applied to each group
def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births/births.sum()
    return group

# Groupby year, sex and get proportion of children
names = names.groupby(['year', 'sex']).apply(add_prop)

# use allclose since we're dealing with floats
np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)


# Get top 1000 names for each year/gender combination
def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]
grouped=names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)

top1000.groupby('year').size()


# Plot some names out
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
total_births = top1000.pivot_table('births', rows='year', cols='name', aggfunc=sum)

subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')

# Plot prop of baby names that fall in to 1000
table = top1000.pivot_table('prop', rows='year', cols='sex', aggfunc=sum)
table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=xrange(1880, 2020, 10))

# Count number of distinct names in top 50% of births
df = boys[boys.year == 1900]
prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()
# ?!? This doesn't work. Already in errata - unconfirmed
# prop_cumsum.searchsorted(0.5)

# Last letters of names
get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'

table = names.pivot_table('births', rows=last_letters, cols=['sex', 'year'], aggfunc=sum)
subtable = table.reindex(columns=[1910, 1969, 2010], level='year')
letter_prop = subtable / subtable.sum().astype(float)
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)

# Using masking
# find all names that start with 'lesl'
# using 'unique'
all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
lesley_like

# filter for 'Leslie' names
filtered = top1000[top1000.name.isin(lesley_like)]
# count how many births with each 'Leslie' name
filtered.groupby('name').births.sum()


table = filtered.pivot_table('births', rows='year', cols='sex', aggfunc='sum')
table = table.div(table.sum(1), axis=0)
table.plot(style={'M' : 'k-', 'F': 'k--'})

