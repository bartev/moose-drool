#
#	overview.py
#	/Users/bvartanian/Development/moose-drool/lrn-pandas/overview.py
#
#	Bartev Vartanian on 2013-12-11
#
# learn to use python from Pandas PyHPC2011.pdf


import numpy as np
import pandas as pd
from pandas import DataFrame

# Create an array
data = array([ ('GOOG', '2009-12-28', 622.87, 1697900.0),
('GOOG', '2009-12-29', 619.40, 1424800.0),
('GOOG', '2009-12-30', 622.73, 1465600.0),
('GOOG', '2009-12-31', 619.98, 1219800.0),
('AAPL', '2009-12-28', 211.61, 23003100.0),
('AAPL', '2009-12-29', 209.10, 15868400.0),
('AAPL', '2009-12-30', 211.64, 14696800.0),
('AAPL', '2009-12-31', 210.73, 12571000.0)],
dtype=[('item', '|S4'), ('date', '|S10'),
       ('price', '<f8'), ('volume', '<f8')])

data['price']

# create a pandas dataframe
data = DataFrame(data)
data

# add a column
data['ind'] = data['item'] == 'GOOG'
data

# delete a column
del data['ind']
data

# pivot on date, time
# each row is a 'date',
# columns for 'item'
data.pivot('date', 'item')

