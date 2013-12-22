import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read JSON file
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()

import json
path
records = [json.loads(line) for line in open(path)]

# access 'tz' column of row 0
records[0]['tz']

# use list comprehension to get all 'tz' items in records
time_zones = [rec['tz'] for rec in records if 'tz' in rec]


# Basic python way of counting items in a list
from collections import defaultdict
def get_counts(seq):
    counts = defaultdict(int)
    for x in seq:
        counts[x] += 1
    return counts

counts = get_counts(time_zones)
len(time_zones)
counts['America/New_York']

# get top 3 items by countsfrom collections import Counter
counts = Counter(time_zones)
counts.most_common(3)

# count with pandas

from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(records)
frame

# 1 liner to get counts of values!
frame['tz'].value_counts()

# cleaning DataFrame
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]

# create a horiz bar chart
tz_counts[:10].plot(kind='barh', rot=0)

# Split strings in column a
results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]


cframe = frame[frame.a.notnull()]
# or
cframe = frame[frame['a'].notnull()]

# get group counts
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
# Note: grouping by another series!
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)

# get indices of sorted array
indexer = agg_counts.sum(1).argsort()

# take(indexer) selects elements in the order of indexer
count_subset = agg_counts.take(indexer)[-10:]
count_subset.plot(kind='barh', stacked=True)


# Normalize to 1
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
# Plot 100% plot
normed_subset.plot(kind='barh', stacked=True)


