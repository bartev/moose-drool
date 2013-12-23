# http://matplotlib.org/1.3.1/examples/pylab_examples/barchart_demo2.html

import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib.ticker import MaxNLocator

student = 'Johnny Doe'
grade = 2
gender = 'boy'
cohortSize = 62

numTests = 5
testNames = ['Pacer Test', 'Flexed Arm\n Hang', 'Mile Run', 'Agility', 'Push Ups']
testMeta = ['laps', 'sec', 'min:sec', 'sec', '']
scores = ['7', '48', '12:52', '17', '14']
rankings = np.round(np.random.uniform(0, 1, numTests) * 100, 0)

fig, ax1 = plt.subplots(figsize=(9, 7))
plt.subplots_adjust(left = 0.115, right=0.88)
fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')
pos = np.arange(numTests) + 0.5
rects = ax1.barh(pos, rankings, align='center', height=0.5, color='m')

ax1.axis([0, 100, 0, 5])
pylab.yticks(pos, testNames)
ax1.set_title('Johnny doe')
plt.text(50, -0.5, 'Cohort Size: ' + str(cohortSize), horizontalalignment='center', size='small')

ax2 = ax1.twinx()
ax2.plot([100, 100], [0, 5], 'white', alpha=0.1)
ax2.xaxis.set_major_locator(MaxNLocator(11))
xticks = pylab.setp(ax2, xticklabels=['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'])
ax2.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.25)
plt.plot([50, 50], [0, 5], 'grey', alpha=0.25)

def withnew(i, scr):
	if testMeta[i] != '':
		return '%s\n' % scr
	else:
		return scr

scoreLabels = [withnew(i, scr) for i, scr in enumerate(scores)]
scoreLabels = [i + j for i, j in zip(scoreLabels, testMeta)]

ax2.set_yticks(pos)
ax2.set_yticklabels(scoreLabels)
ax2.set_ylim(ax1.get_ylim())

ax2.set_ylabel('Test Scores')

suffixes = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']
ax2.set_xlabel('Percentile Ranking Across ' + str(grade) + suffixes[grade] + ' Grade ' + gender.title() + 's')

for rect in rects:
	width = int(rect.get_width())
	lastDigit = width % 10
	if (width == 11) or (width == 12) or (width == 13):
		suffix = 'th'
	else:
		suffix = suffixes[lastDigit]
	rankStr = str(width) + suffix
	if (width < 25):
		xloc = width + 1
		clr = 'black'
		align = 'left'
	else:
		xloc = 0.98 * width
		clr = 'white'
		align = 'right'
	
	yloc = rect.get_y() + rect.get_height() / 2.0
	ax1.text(xloc, yloc, rankStr, horizontalalignment=align, verticalalignment='center', color=clr, weight='bold')

plt.show()








