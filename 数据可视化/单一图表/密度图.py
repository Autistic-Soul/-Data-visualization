# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:11:55 2018

@author: student02
"""

from pandas import read_csv
import matplotlib.pyplot as plt
a = 'q.csv'
b = ['1','2','3','4','5','6','7']
data = read_csv(a ,names = b)
data.plot(kind = 'box', subplots = True , layout = (3,3), sharex = False)
plt.show()