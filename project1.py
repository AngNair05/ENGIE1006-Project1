#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:40:33 2024

@author: angelinanair
"""

import csv

file = open('air_quality.csv', 'r')
dic = {}
dic2 ={}

for i in file: 
    values = i.strip().split(",")
    
    if values:
        key = values[0] 
        key1 = values[2]
        
        tuple_values = tuple(values[3:])  
        tuple_values1 = tuple(values[3:])
        
        if key in dic:
            dic[key].append(tuple_values)
            
        else:
            dic[key] = [tuple_values] 
        
        #for second dictionary
        if key1 in dic2:
            dic2[key1].append(tuple_values1)
        else:
            dic2[key1] = [tuple_values1]  
  
    
#print(dic)
print(dic2)



file.close()