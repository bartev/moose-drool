Sample = range(1, 11)
Gender =['Female','Male', 'Female', 'Male','Male','Male','Female','Female','Male','Female']
Handedness  = ['Right-handed',  'Left-handed',  'Right-handed',  'Right-handed',  'Left-handed',  'Right-handed',  'Right-handed',  'Left-handed',  'Right-handed',  'Right-handed']
data = {'Sample': Sample, 'Gender': Gender, 'Handedness': Handedness}
data = DataFrame(data, columns = ['Sample', 'Gender', 'Handedness'])

pd.crosstab(data.Gender, data.Handedness, margins=True)