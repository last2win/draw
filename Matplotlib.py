# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:27:52 2019

@author: peter
"""

import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
y = [5, 20, 36, 10, 75, 90]
plt.title("商家A")
plt.bar(x, y)
plt.show()
