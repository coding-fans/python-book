#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   read_qrcode.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

from PIL import Image
import zbarlight

# 二维码图片路径
file_path = './zedhz-course-qrcode.jpg'

# 读取文件
with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()

# 识别二维码
codes = zbarlight.scan_codes('qrcode', image)
print('QR codes: %s' % codes)
