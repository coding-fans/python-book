#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   font.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.font_manager as mfm

fonts = (
    ('微软雅黑', 'Downloads/Microsoft Yahei.ttf',),
    ('中易黑体', 'Downloads/SimHei.ttf',),
    ('仿宋', 'Downloads/FangSong.ttf',),
    ('宋体', 'Downloads/STSong.ttf',),
)

# load font files
label_fonts = tuple(
    mfm.FontProperties(fname=path, size=10)
    for _, path in fonts
)

title_fonts = label_fonts[0].copy()
title_fonts.set_size(18)

# data to plot
labels = [name for name, _ in fonts]
sizes = (215, 130, 245, 210,)

colors = ('gold', 'yellowgreen', 'lightcoral', 'lightskyblue',)

patches, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
)

for text, font in zip(texts, label_fonts):
    text.set_fontproperties(font)

plt.title("编程语言", fontproperties=title_fonts)

plt.show()
