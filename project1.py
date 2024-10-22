#function for dictionaries
def geo_measurement(filename, dict_num):
    f = open(filename+'.csv', 'r')
    geo_to_measurement = {}
    date_to_measurement = {}
    uhf_to_place_name = {}
    zip_to_UHF = {}
    borough_to_UHF = {}
    
    #first dictionary, geographic ID to measurement
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
    
    #second dictionary, date to measurements
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
        
    #third dictionary, UHF ID to place name
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
    
    #fourth dictionary, zipcode to UHF ID
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
    
    #fifth dictionary, borough name to UHF ID
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

#call functions
uhf_to_measurement = geo_measurement("air_quality", 1)
date_to_measurement = geo_measurement("air_quality", 2)
uhf_to_place_name = geo_measurement("air_quality", 3)
zip_to_uhf = geo_measurement("uhf", 4)
borough_to_uhf = geo_measurement("uhf", 5)

#part 1c), sorting the data by user input
if __name__ == "__main__":
    #obtain user input
    user_choice = input("Would you like to search the data by zip code (z), UHF ID (u), borough(b), or date(d)? ")
    
    #invalid input
    while(not user_choice in "zubd"):
        print("Please enter a valid key.")
        user_choice = input("Would you like to search the data by zip code (z), UHF ID (u), borough(b), or date(d)? ")
        
    #sort by zipcode
    if user_choice == 'z':
        user_zipcode = input("What is the zipcode? ")
        #invalid zipcode
        while (not user_zipcode in zip_to_uhf):
            print("No data could be find for that zipcode. Please enter another zipcode.")
            user_zipcode = input("What is the zipcode? ")
    
        for i in zip_to_uhf[user_zipcode]:
            for j in uhf_to_measurement[i]:
                print(j[2], "UHF", j[0], j[1], j[3], "mcg/m^3")    
        
    
    #sort by UHF ID
    if user_choice == 'u':
        user_uhf = input("What is the UHF ID? ")
        #invalid input
        while (not user_uhf in uhf_to_measurement):
            print("No data could be find for that UHF ID. Please enter another UHF.")
            user_uhf = input("What is the UHF ID? ")
        
        for i in uhf_to_measurement[user_uhf]:
            print(i[2], "UHF", i[0], i[1], i[3], "mcg/m^3")
        
    #sort by borough
    if user_choice == 'b':
        user_borough = input("What is the borough? ")
        #invalid borough
        while (not user_borough in borough_to_uhf):
            print("No data could be find for that place. ")
            user_borough = input("What is the borough? ")
    
        for i in borough_to_uhf[user_borough]:
            for j in uhf_to_measurement[i]:
                print(j[2], "UHF", j[0], j[1], j[3], "mcg/m^3") 
    
        
    #sort by date
    if user_choice == 'd':
        user_date = input("What is the date? (Enter it in y/m/dd format) ")
        #invalid date
        while (not user_date in date_to_measurement):
            print("No data could be find for that date. Please enter another day in the correct format.")
            user_date = input("What is the date? (Enter it in y/m/dd format) ")
            
        for i in date_to_measurement[user_date]:
            print(user_date, "UHF", i[0], i[1], i[3], "mcg/m^3")

