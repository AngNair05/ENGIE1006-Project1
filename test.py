#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:19:25 2024

@author: angelinanair
"""

def read_air_quality_data(filename):
    uhf_to_measurement = {}
    date_to_measurement = {}
    
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split(",")
            
            uhf_id = values[0]
            date = values[2]
            measurement_tuple = tuple(values[3:])
            
            add_to_dict(uhf_to_measurement, uhf_id, measurement_tuple)
            add_to_dict(date_to_measurement, date, measurement_tuple)
    
    return uhf_to_measurement, date_to_measurement

def read_uhf_data(filename):
    zip_to_UHF = {}
    borough_to_UHF = {}
    
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split(",")
            
            zipcode = values[1]
            borough_name = values[0]
            
            for key in values[3:]:
                add_to_dict(zip_to_UHF, key, zipcode)
            
            add_unique_to_dict(borough_to_UHF, borough_name, zipcode)
    
    return zip_to_UHF, borough_to_UHF

def add_to_dict(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]

def add_unique_to_dict(dictionary, key, value):
    if key in dictionary:
        if value not in dictionary[key]:
            dictionary[key].append(value)
    else:
        dictionary[key] = [value]

# Call the functions
uhf_to_measurement, date_to_measurement = read_air_quality_data('air_quality.csv')
zip_to_UHF, borough_to_UHF = read_uhf_data('uhf.csv')

# Print the results
print("UHF to Measurement:", uhf_to_measurement)
print("Date to Measurement:", date_to_measurement)
print("Zip to UHF:", zip_to_UHF)
print("Borough to UHF:", borough_to_UHF)
