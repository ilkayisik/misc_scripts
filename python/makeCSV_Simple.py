#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:14:45 2018

@author: ilkay.isik
"""
import csv
y = [1,2,3,4,5]
csvfile = 'xxx.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in y:
        writer.writerow([val])