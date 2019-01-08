#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   pie.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# data to plot
labels = ('Python', 'C++', 'Ruby', 'Java',)
sizes = (215, 130, 245, 210,)

colors = ('gold', 'yellowgreen', 'lightcoral', 'lightskyblue',)

plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
)

plt.title("Programming Languages")

plt.show()
