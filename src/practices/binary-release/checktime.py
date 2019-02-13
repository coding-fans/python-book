#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   checktime.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import ntplib

from datetime import (
    datetime,
)

def format_ts(ts):
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def check_time():
    client = ntplib.NTPClient()
    rsps = client.request('asia.pool.ntp.org', version=3)

    print('Server:', ntplib.ref_id_to_text(rsps.ref_id))
    print('Offset:', rsps.offset)
    print('Time:', format_ts(rsps.tx_time))

if __name__ == '__main__':
    check_time()
