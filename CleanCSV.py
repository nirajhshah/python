# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:18:23 2016

@author: nshah
"""

import csv

input = open('C:\SF_workassignment\sf_6_8_2018\OldData.csv', 'r',encoding='utf8')
output = open('C:\SF_workassignment\sf_6_8_2018\Cleaned_Data.csv', 'w')
writer = csv.writer(output)
for row in csv.reader(input):
    if row:
        writer.writerow(row)
input.close()
output.close()