#!/usr/bin/env python

from operator import itemgetter
import sys
import datetime

#make a dictionary to hold a list of differences for each system id
#initialize the dictionary with the various systemid's
dict = {k:[] for k in ['1','2','3','4','5','6','7','8','9','10','11',                                              '12','13','14','15','16','17','18','19','20']}

#AM = datetime.datetime.strptime("09:00:00", '%H:%M:%S')
#PM = datetime.datetime.strptime("17:00:00", '%H:%M:%S')

#get input from standard input
for line in sys.stdin:

        # clean up whitespace
        line = line.strip()

        #parse mapper input
        array = line.split(' ')
        array = [index.strip() for index in array]

        if array:
            try:
                timeofday = str(array[1])
                timeofday = timeofday.replace(':','')
                systemid = int(array[3])
                actual = int(array[5])
            except ValueError:
                    continue

        #only add temps during business hours
        if (90000 <= int(timeofday) <= 170000):       
        	#add the temperatures for each system id to a designated list 
	 	dict[str(systemid)].append(int(actual))
	

#create a new dictionary that holds the average temp as the value for each system id
dict1 = {k:float((sum(v)))/len(v) for k, v in dict.items()}

#print out the worst 3 system id's and their average deviation                              
sorted_dict = (sorted(dict1.items(), key=lambda x: x[1], reverse = True))[:3]
print("Below are the 3 hottest buidings in the format (SystemID,averageTemp):")
print(sorted_dict)
