#Part 2 Meri

from project1 import geo_measurement  
    
#Part 2 a)
#Find highest and lowest pollution measurement ever recorded in zip code 10027

print("\nPart 2\na) Highest and lowest pollution measurement ever recorded in zip code 10027:")

#Step 1: finding the UHF the zip code 10027 corresponds to:
zip_chosen_to_uhf = geo_measurement("uhf", 4) #creating the dictionary that maps zip code to UHF

zip_chosen_to_uhf = zip_chosen_to_uhf["10027"][0] #finding the UHF that corresponds to zip code 10027 -> result is string '302'


#Step 2: Using the UHF to measurements dictionary, find the min & max measurements corresponding to UHF 302

#create uhf_to_measurement dictionary
uhf_to_measurement = geo_measurement("air_quality", 1)

#Finding the smallest measurement with UHF 302 (zip code 10027)
min_measurement = float((uhf_to_measurement[zip_chosen_to_uhf])[0][3]) #setting a min value and converting to float data type

for element in uhf_to_measurement[zip_chosen_to_uhf]: #iterating through the tuples of measurements with UHF 302
    if float(element[3]) < min_measurement:
        min_measurement = float(element[3])
    
print("\t--> Lowest pollution measurement ever recorded in zip code 10027: ", min_measurement)
    

#Finding the largest measurement with UHF 302 (zip code 10027)
max_measurement = float((uhf_to_measurement[zip_chosen_to_uhf])[0][3]) #setting a max value and converting to float data type

for element in uhf_to_measurement[zip_chosen_to_uhf]: #iterating through the tuples of measurements with UHF 302
    
    if float(element[3]) > max_measurement:
        max_measurement = float(element[3])
    
print("\t--> Largest pollution measurement ever recorded in zip code 10027: ", max_measurement)


#______________________________________________________________________________________________________
#part 2 b) Which UHF id had the worst pollution in 2019.

print("\nb) Which UHF id had the worst pollution in 2019?")

#Step 1: extract the measurements for 2019
#create date_to_measurement dictionary
date_to_measurement = geo_measurement("air_quality", 2)


lists_data_2019 = [] #creating a list with lists that store all tuplres for a specific date (in this case 2 sublists because we have only 2 diffferent dates)

for key in date_to_measurement:
    
    if key[len(key)-1:len(key)-3:-1] == "91": 
        
        lists_data_2019.append(date_to_measurement[key]) #creates a list with 2 lists inside - first list for 6/1 and second for 12/1


list_tuples_measurements_2019 = [] #creating only 1 list with all the tuple measurements for 2019
index = 0

while (index < len(lists_data_2019)):
    list_tuples_measurements_2019 = list_tuples_measurements_2019 + lists_data_2019[index]
    index += 1
    

#Step 2: Find the worst (highest) pollution value in the data for 2019

worst_pollution_max_value = float(list_tuples_measurements_2019[0][3])

for element in list_tuples_measurements_2019:
    if float(element[3]) > worst_pollution_max_value:
       worst_pollution_max_value = float(element[3])
      
print("\t--> Value for the worst pollution in 2019:" , worst_pollution_max_value)


#Step 3: Printing the UHF ID associated with the value for worst pollution in 2019
for element in list_tuples_measurements_2019:
    if float(element[3]) == worst_pollution_max_value:
        print ("\t--> UHF ID with worst pollution in 2019:", element[0])



#______________________________________________________________________________________________________
#part 2 c) What was the average air pollution in Manhattan in 2008 and in 2019.

print("\nc) What was the average air pollution in Manhattan in 2008 and in 2019?")

#Step 1: Finding UHFs corresponding to Manhattan

#create dictionary borough_to_uhf
borough_to_uhf = geo_measurement("uhf", 5)

#finding what UHFs that belong to Manhattan and storing them in a list
list_manhattan_uhfs = []

for key in borough_to_uhf:
    if key == "Manhattan":
        list_manhattan_uhfs = list_manhattan_uhfs + borough_to_uhf[key]
    

#Step 2: Finding tuples of measurements corresponding to Manhattan UHFs

#finding all the tuples of measurements that belong to the Manhattan UHFs and storing them in one list of tuples with measurements
list_tuples_data_for_each_Manhattan_uhf = []

for element in list_manhattan_uhfs:
    list_tuples_data_for_each_Manhattan_uhf = list_tuples_data_for_each_Manhattan_uhf + uhf_to_measurement[element]
    

#Sftep 3: Iterating over the list of tuples with measurements for Manhattan and finding their sum and count and avg for 2008 and 2019

#average for 2008
sum_measurements_2008 = 0
count_measurements_2008 = 0
for element in list_tuples_data_for_each_Manhattan_uhf:
    if element[2][len(element[2])-1:len(element[2])-3:-1] == '80': #finding data for 2008, string endning in 08
        sum_measurements_2008 = sum_measurements_2008 + float(element[3])
        count_measurements_2008 +=1
        
average_for_2008 = sum_measurements_2008 / count_measurements_2008
        
print("\t--> Average air pollution in Manhattan in 2008 =", average_for_2008)


#average for 2019
sum_measurements_2019 = 0
count_measurements_2019 = 0
for element in list_tuples_data_for_each_Manhattan_uhf:
    if element[2][len(element[2])-1:len(element[2])-3:-1] == '91': #finding data for 2019, string ending in 19
        sum_measurements_2019 = sum_measurements_2019 + float(element[3])
        count_measurements_2019 +=1
        
average_for_2019 = sum_measurements_2019 / count_measurements_2019
        
print("\t--> Average air pollution in Manhattan in 2019 =", average_for_2019)




#______________________________________________________________________________________________________
#part 2 d) What was the average air pollution in Bronx in 2010
print("\nd) Personal queries:\n\t1.What was the average air pollution in Bronx in 2010?")

#borough_to_uhf dictionary created in c)

#finding what UHFs that belong to Bronx and storing them in a list
list_Bronx_uhfs = []

for key in borough_to_uhf:
    if key == "Bronx":
        list_Bronx_uhfs = list_Bronx_uhfs + borough_to_uhf[key]

#finding all the tuples of measurements for all years that belong to the Bronx UHFs and storing them in a list of tuples with measurements
list_tuples_data_for_each_Bronx_uhf = []

for element in list_Bronx_uhfs:
        list_tuples_data_for_each_Bronx_uhf = list_tuples_data_for_each_Bronx_uhf + uhf_to_measurement[element]
    
#Finding average for 2010
sum_measurements_2010 = 0
count_measurements_2010 = 0
for element in list_tuples_data_for_each_Bronx_uhf:
    if element[2][len(element[2])-1:len(element[2])-3:-1] == '01': #extracting the data for 2010
        sum_measurements_2010 = sum_measurements_2010 + float(element[3])
        count_measurements_2010 += 1

average_for_2010 = sum_measurements_2010 / count_measurements_2010
        
print("\t --> Average air pollution in Bronx in 2010 =", average_for_2010)


#______________________________________________________________________________________________________
#part 2 d) What was the range for air pollution in Bronx in 2010
print("\n\t2.What was the range for air pollution in Bronx in 2010?")

#using the list of data created for Bronx for all years from part d) 1

#create a lift for data for Bronx in 2010 only
list_tuples_data_for_each_Bronx_uhf_2010 = []

for element in list_tuples_data_for_each_Bronx_uhf:
    if element[2][len(element[2])-1:len(element[2])-3:-1] == '01': #extracting the data for 2010
       list_tuples_data_for_each_Bronx_uhf_2010.append(element)
        

#Finding MIN measurement for Bronx in 2010:
min_measurement = float(list_tuples_data_for_each_Bronx_uhf_2010[0][3])

for element in list_tuples_data_for_each_Bronx_uhf_2010:
        if float(element[3]) < min_measurement:
            min_measurement = float(element[3])
        
print("\t --> Smallest measurement in Bronx in 2010:", min_measurement)


#Finding MAX measurement for Bronx in 2010:
max_measurement = float(list_tuples_data_for_each_Bronx_uhf_2010[0][3])

for element in list_tuples_data_for_each_Bronx_uhf_2010:
        if float(element[3]) > max_measurement:
            max_measurement = float(element[3])
        
print("\t --> Largest measurement in Bronx in 2010:", max_measurement)

range_value = max_measurement - min_measurement

#Finding range
print("\t --> Range for measurements in Bronx in 2010:", range_value)
