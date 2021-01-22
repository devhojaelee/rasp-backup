#!/usr/bin/env python
#!/bin/bash
# -*- coding: utf-8 -*-

import os 
import sys
import datetime

base_path = '/mnt/gsuite/rasp_backup/'
backup_file = ''
backup_list_full = ['/bin','/etc','/lib','/media','/opt','/root','/sbin','/sys','/usr','/boot','/dev','/proc','/run','/srv','/tmp','/var','/home/pi']
#backup_list_full = ['/home/pi/project'] 
backup_file = base_path +datetime.datetime.now().strftime('%y-%m-%d_%H:%M')+ '_'+sys.argv[1] + '.tar.gz'
os.system('tar cvfz ' + backup_file + ' ' + ' '.join(backup_list_full))
