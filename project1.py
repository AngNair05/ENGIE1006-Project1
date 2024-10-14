#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:40:33 2024

@author: angelinanair
"""

import csv

file = open('air_quality.csv', 'r')

for i in range(10): # print the first 10 lines 
    print(file.readline().strip())
file.close()