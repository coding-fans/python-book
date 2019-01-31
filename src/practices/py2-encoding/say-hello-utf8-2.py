#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   say-hello-utf8-2.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import sys
reload(sys)
sys.setdefaultencoding('UTF8')

print u'你好，世界！'
