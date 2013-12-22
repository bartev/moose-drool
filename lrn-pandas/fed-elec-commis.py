fec = pd.read_csv('pydata-book/ch09/P00000001-ALL.csv')

fec.ix[123456]

# Get unique candidates
unique_cands = fec.cand_nm.unique()
unique_cands

parties = {'Bachmann, Michelle': 'Republican', 'Cain, Herman': 'Republican', 'Gingrich, Newt': 'Republican', 'Huntsman, Jon': 'Republican', 'Johnson, Gary Earl': 'Republican', 'McCotter, Thaddeus G': 'Republican', 'Obama, Barack': 'Democrat', 'Paul, Ron': 'Republican', 'Pawlenty, Timothy': 'Republican', 'Perry, Rick': 'Republican', "Roemer, Charles E. 'Buddy' III": 'Republican', 'Romney, Mitt': 'Republican', 'Santorum, Rick':'Republican'}

# Select a group of contributors (rows)
fec.cand_nm[123456:123461]
# map the parties
fec.cand_nm[123456:123461].map(parties)
# Assign this to a new column
fec['party'] = fec.cand_nm.map(parties)
# count how many contributors per party
fec['party'].value_counts()

# Donations & refunds
(fec.contb_receipt_amt > 0).value_counts()
# Restrict to donations
fec = fec[fec.contb_receipt_amt > 0]
# Separate out donations to Obama and Romney
fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]

# Count contributions by occupation
occ_mapping = {
	'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED', 
	'INFORMATION REQUESTED' : 'NOT PROVIDED',
	'INFORMATION REQUESTED (BEST EFFORTS)' : 'NOT PROVIDED', 
	'C.E.O.': 'CEO'
	}
# If no mapping provided, return x
f = lambda x: occ_mapping.get(x, x) 
fec.contbr_occupation = fec.contbr_occupation.map(f)


emp_mapping = {
	'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED', 
	'INFORMATION REQUESTED' : 'NOT PROVIDED',
	'SELF' : 'SELF-EMPLOYED',
	'SELF EMPLOYED' : 'SELF-EMPLOYED',
	}
	
# If no mapping provided, return x
f = lambda x: emp_mapping.get(x, x) 
fec.contbr_employer = fec.contbr_employer.map(f)

by_occupation = fec.pivot_table('contb_receipt_amt', rows='contbr_occupation', cols='party', aggfunc='sum')
over_2mm = by_occupation[by_occupation.sum(1) > 2e6]
over_2mm


def get_top_amounts(group, key, n=5):
	totals = group.groupby(key)['contb_receipt_amt'].sum()
	# Order totals by key in descending order 
	return totals.order(ascending=False)[:n]


grouped = fec_mrbo.groupby('cand_nm')
# Top 7 by occupation
grouped.apply(get_top_amounts, 'contbr_occupation', n=7)
# Topy 10 by employer
grouped.apply(get_top_amounts, 'contbr_employer', n=10)


# bucketing
bins = np.array([0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
labels = pd.cut(fec_mrbo.contb_receipt_amt, bins)
grouped = fec_mrbo.groupby(['cand_nm', labels])

grouped.size().unstack(0)
bucket_sums = grouped.contb_receipt_amt.sum().unstack(0)
normed_sums = bucket_sums.div(bucket_sums.sum(axis=1), axis=0)
normed_sums[:-2].plot(kind='barh', stacked=True)


grouped = fec_mrbo.groupby(['cand_nm', 'contbr_st'])
totals = grouped.contb_receipt_amt.sum().unstack(0).fillna(0)
totals = totals[totals.sum(1) > 1e5]
percent = totals.div(totals.sum(1), axis=0)

from mpl_toolkits.basemap import Basemap, cm 
import numpy as np
from matplotlib import rcParams
from matplotlib.collections import LineCollection 
import matplotlib.pyplot as plt
from shapelib import ShapeFile 
import dbflib
obama = percent['Obama, Barack']
fig = plt.figure(figsize=(12, 12)) 
ax = fig.add_axes([0.1,0.1,0.8,0.8])
lllat = 21; urlat = 53; lllon = -118; urlon = -62