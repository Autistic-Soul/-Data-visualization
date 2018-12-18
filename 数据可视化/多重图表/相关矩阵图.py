# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:11:55 2018

@author: student02
"""

from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np
a = 'q.csv'
b = ['1','2','3','4','5','6','7']
data = read_csv(a ,names = b)
correlations = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations,vmin = -1,vmax = 1)
fig.colorbar(cax)
ticks = np.arange(0,7,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(b)
ax.set_yticklabels(b)
plt.show()