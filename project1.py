#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:40:33 2024

@author: angelinanair
"""

file = open('air_quality.csv', 'r')
uhf_to_measurement = {}
date_to_measurement = {}
uhf_to_place_name = {}

for i in file: 
    values = i.strip().split(",")
    
    uhf_id = values[0] 
    place_name = values[1]
    date = values[2]
    
    measurement_tuple = tuple(values[3:])  
    
    if uhf_id in uhf_to_measurement:
        uhf_to_measurement[uhf_id].append(measurement_tuple)
        
    else:
        uhf_to_measurement[uhf_id] = [measurement_tuple] 
    
    #for second dictionary
    if date in date_to_measurement:
        date_to_measurement[date].append(measurement_tuple)
    else:
        date_to_measurement[date] = [measurement_tuple] 
        
        
        
    # if bourough_name in borough_to_UHF:
    #     if zipcode not in borough_to_UHF[bourough_name]:
    #         borough_to_UHF[bourough_name].append(zipcode)  
    # else: 
    #     borough_to_UHF[bourough_name] = [zipcode]
        
    #third dictionary that maps geo id to place name 
    
    if uhf_id in uhf_to_place_name:
        if place_name not in uhf_to_place_name[uhf_id]:
            uhf_to_place_name[uhf_id].append(place_name)
    else: 
        uhf_to_place_name[uhf_id] = [place_name]
  
    
#print(uhf_to_measurement)
#print(date_to_measurement)
print(uhf_to_place_name)

file.close()

file2 = open('uhf.csv', 'r')
zip_to_UHF = {}
borough_to_UHF = {}

for x in file2: 
    value = x.strip().split(",")
    

    zipcode = value[2]
    bourough_name = value[0]
    
    for key in value[3:]:
        if key in zip_to_UHF:
            zip_to_UHF[key].append(zipcode)
        else:
            zip_to_UHF[key] = [zipcode]
                            
    #second dictionary 
    if bourough_name in borough_to_UHF:
        if zipcode not in borough_to_UHF[bourough_name]:
            borough_to_UHF[bourough_name].append(zipcode)  
    else: 
        borough_to_UHF[bourough_name] = [zipcode]
    
    

#print(zip_to_UHF)
#print(borough_to_UHF)
file2.close()
