# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:40:05 2023

@author: shiduyule
"""

# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# fruits = ['A1', 'A2', 'A3', 'A4','A5','A6']
# counts = [40, 100, 30, 55,64,55]
# bar_labels = ['orange','blue']
# bar_colors = ['tab:orange', 'tab:blue']

# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

# ax.set_ylabel('fruit supply')
# ax.set_title('Fruit supply by kind and color')
# ax.legend(title='Fruit color')

# plt.show()

##     'RMS': (6.22797E-6,3.97262E-6,9.10919E-6,1.13261E-5,1.37906E-5,1.04447E-5),
##    'AVG': (4.23864E-6,2.01698E-6,5.62524E-6,5.93133E-6,8.31132E-6,6.19266E-6),
import matplotlib.pyplot as plt
import numpy as np

species = ("RMS", "AVG")
data = {
    
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(dpi = 600)  # constrained_layout=True,

for zhibiao, shuzhi in data.items():  #  键值对
    offset = width * multiplier
    rects = ax.bar(x + offset, shuzhi, width, label=zhibiao)
    ax.bar_label()  # rects, padding=3
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)

plt.show()
