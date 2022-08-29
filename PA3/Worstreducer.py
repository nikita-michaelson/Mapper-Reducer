#!/usr/bin/env python

from operator import itemgetter
import sys


#make a dictionary to hold a list of differences for each system id
#initialize the dictionary with the various systemid's
dict = {k:[] for k in ['1','2','3','4','5','6','7','8','9','10','11',
                       '12','13','14','15','16','17','18','19','20']}

#get input from standard input
for line in sys.stdin:
    # clean up whitespace
    line = line.strip()
    #parse mapper input
    array = line.split(' ')
    array = [index.strip() for index in array]

    if array:
        
        try:
            systemid = int(array[1])
            desired = int(array[3])
            actual = int(array[5])            
        except ValueError:
            continue
        
        #difference between actual and desired temp
        diff = abs((actual - desired))

        #add associated differences to list
        dict[str(systemid)].append(diff)
        
#create a new dictionary that holds the original keys but makes the values the average diff
dict1 = {k:float((sum(v)))/len(v) for k, v in dict.items()}

#print out the worst 3 system id's and their average deviation
print("Below are the worst performing HVAC systems in the format (SystemID,averageDifferenceInTemp):")
print(sorted(dict1.items(), key=lambda x: x[1], reverse = True))[:3]
