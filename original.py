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
    
    measurement_tuple = tuple(values[0:])  
    
    if uhf_id in uhf_to_measurement:
        if measurement_tuple not in uhf_to_measurement[uhf_id]:
            uhf_to_measurement[uhf_id].append(measurement_tuple)
    else:
        uhf_to_measurement[uhf_id] = [measurement_tuple] 
    
    #for second dictionary
    if date in date_to_measurement:
        date_to_measurement[date].append(measurement_tuple)
    else:
        date_to_measurement[date] = [measurement_tuple] 
        
        
    #third dictionary that maps geo id to place name 
    if uhf_id in uhf_to_place_name:
        if place_name not in uhf_to_place_name[uhf_id]:
            uhf_to_place_name[uhf_id].append(place_name)
    else: 
        uhf_to_place_name[uhf_id] = [place_name]
  

def geo_measurement(filename, dict_num):
    f = open(filename+'.csv', 'r')
    geo_to_measurement = {}
    date_to_measurement = {}
    uhf_to_place_name = {}
    zip_to_UHF = {}
    borough_to_UHF = {}
    
    #first dictionary 
    if dict_num == 1: 
        for i in f: 
            values = i.strip().split(",")
            uhf_id = values[0]
            measurement = tuple(values[0:])  
        
            if uhf_id in geo_to_measurement:
                if measurement not in geo_to_measurement[uhf_id]:
                    geo_to_measurement[uhf_id].append(measurement)
            else:
                geo_to_measurement[uhf_id] = [measurement] 
            
        return geo_to_measurement
    
    #second dictionary
    if dict_num == 2: 
        for i in f: 
            values = i.strip().split(",")
            date = values[2]
            measurement_tuple = tuple(values[0:])  
            if date in date_to_measurement:
                date_to_measurement[date].append(measurement_tuple)
            else:
                date_to_measurement[date] = [measurement_tuple] 
        return date_to_measurement
        
    #3rd
    if dict_num == 3: 
        for i in f: 
            values = i.strip().split(",")
            uhf_id = values[0]
            place_name = values[1]
            
            if uhf_id in uhf_to_place_name:
                if place_name not in uhf_to_place_name[uhf_id]:
                    uhf_to_place_name[uhf_id].append(place_name)
            else: 
                uhf_to_place_name[uhf_id] = [place_name]
                
        return uhf_to_place_name
    
    #4th
    if dict_num == 4: 
        for i in f: 
            values = i.strip().split(",")
            zipcode = values[2]
            for key in values[3:]:
                if key in zip_to_UHF:
                    zip_to_UHF[key].append(zipcode)
                else:
                    zip_to_UHF[key] = [zipcode]
        return zip_to_UHF
    
    #5th
    if dict_num == 5: 
        for i in f: 
            values = i.strip().split(",")
            zipcode = values[2]
            bourough_name = values[0]

            if bourough_name in borough_to_UHF:
                if zipcode not in borough_to_UHF[bourough_name]:
                    borough_to_UHF[bourough_name].append(zipcode)  
            else: 
                borough_to_UHF[bourough_name] = [zipcode]
        return borough_to_UHF
            
        
#print("UHF Geo codes to their measurements: ", geo_measurement("air_quality",1), "\n")
#print("Dates to measurements: ", geo_measurement("air_quality",2), "\n")
#print("UHF Geo code to the place name: ", geo_measurement("air_quality",3), "\n")

print("Zipcode to UHF geo code: ", geo_measurement("uhf",4), "\n")
print("Borough name to UHF geo code: ", geo_measurement("uhf",5))

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
    
    

#print("Zipcode to UHF geo code: ", zip_to_UHF, "\n")
#print("Borough name to UHF geo code: ", borough_to_UHF)
file2.close()
