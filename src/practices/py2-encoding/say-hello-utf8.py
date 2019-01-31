#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   say-hello-utf8.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import codecs
import sys

sys.stdout = codecs.getwriter('utf8')(sys.stdout)

print u'你好，世界！'
