#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   stdio-encoding.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import sys

for name in ('stdin', 'stdout', 'stderr'):
    print name, getattr(sys, name).encoding
