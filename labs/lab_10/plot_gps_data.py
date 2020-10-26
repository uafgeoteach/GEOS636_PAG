#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
from datetime import datetime
from numpy    import genfromtxt

filename = sys.argv[1]
site     = filename[:4]

data     = genfromtxt(filename, encoding='utf-8', dtype=None, delimiter=',', skip_header=12, names=['date', 'north', 'east', 'vertical', 'nStd', 'eStd', 'vStd', 'quality', 'dummy'])
dates    = [datetime.strptime(x, '%Y-%m-%d') for x in data['date']]

plt.subplot(3,1,1)
plt.errorbar(dates, data['north'], yerr=data['nStd'], fmt='.', ecolor='gray')
plt.ylabel('north displacement (mm)')
plt.title('site %s from %s' % (site, filename))

plt.subplot(3,1,2)
plt.errorbar(dates, data['east'], yerr=data['eStd'], fmt='.', ecolor=[0.5,0.5,0.5])
plt.ylabel('east (mm)')

plt.subplot(3,1,3)
plt.errorbar(dates, data['vertical'], yerr=data['vStd'], fmt='.', ecolor='0.5')
plt.ylabel('vertical (mm)')
plt.xlabel('date')

print("Saving figure '"+filename+".png'")
plt.savefig(filename+'.png')

plt.show()
