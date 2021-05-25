# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:42:19 2021

@author: I515157
"""

import os
import argparse

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

parser = argparse.ArgumentParser()
parser.add_argument('--number', type=int, default='0', help='number of images')
parser.add_argument('--folder', type=str, default='valid', help='number of images')

opt = parser.parse_args()    
number = opt.number
mydir = opt.folder + '/'

filelist = [ f for f in os.listdir(mydir) if is_number(f.split('.')[0]) and int(f.split('.')[0]) > number]
for f in filelist:
    os.remove(os.path.join(mydir, f))