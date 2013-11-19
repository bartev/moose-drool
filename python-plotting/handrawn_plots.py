import numpy as np
import pylab as pl
from scipy import interpolate, signal
import matplotlib.font_manager as fm

import os
import urllib2
if not os.path.exists('Humor-Sans.ttf'):
    fhandle = urllib2.urlopen('http://antiyawn.com/uploads/Humor-Sans.ttf')
    open('Humor-Sans.ttf', 'wb').write(fhandle.read())
