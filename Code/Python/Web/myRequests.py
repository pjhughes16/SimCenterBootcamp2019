import requests
import numpy as np
import csv

# function definitions
def printBldg(theBldg):

    # name
    #if 'name' in theBldg:
    print(theBldg['name'],': {')
    #else:
    #    print('"Building Name":\t "N/A"')

    # occupancy type
    if 'occupancy' in theBldg:
        print('\t"Occupancy Type":\t"', theBldg['occupancy'],'",')
    else:
        print('\"tOccupancy Type":\t "N/A"')

    # postal address
    if 'address' in theBldg:
        print('\t"Address":\t\t"', theBldg['address'],'",')
    else:
        print('\t"Address":\t\t "N/A"')

    # completion date
    if 'completion_date' in theBldg:
        print('\t"Construction Date":\t', theBldg['completion_date'],',')
    else:
        print('\t"Construction Date":\t "N/A"')

     # number of stories
    if 'stories_above_grade' in theBldg:
        print('\t"Number of stories":\t', theBldg['stories_above_grade'],',')
    else:
        print('\t"Number of stories":\t "N/A"')

    # height
    if 'height_ft' in theBldg:
        print('\t"Height":\t\t', theBldg['height_ft'],',')
    else:
        print('\t"Height":\t\t "N/A"')

    # square footage
    if 'square_footage' in theBldg:
        print('\t"Total Floor Area":\t', theBldg['square_footage'],',')
    else:
        print('\t"Total Floor Area":\t "N/A"')

    # polygon
    if 'polygon' in theBldg:
        if 'coordinates' in theBldg['polygon']:
            print('\t"Coordinates": {')
            for i in range(0,len(theBldg['polygon']['coordinates'][0])):
                print('\t\tLong ',i+1,':\t',theBldg['polygon']['coordinates'][0][i][0],',')
            for i in range(0,len(theBldg['polygon']['coordinates'][0])):
                if i != (len(theBldg['polygon']['coordinates'][0]) - 1):
                    print('\t\tLat  ',i+1,':\t',theBldg['polygon']['coordinates'][0][i][1],',')
                else:
                    print('\t\tLat  ',i+1,':\t',theBldg['polygon']['coordinates'][0][i][1])
        else:
            print('\t"Coordinates":\t\t "N/A"')
    else:
        print('\t"Coordinates":\t\t "N/A"')

    print('\t}')

    # finish formatting
    print('}')
    print('\n')


#Let's request the tall buildings information
response = requests.get('https://data.sfgov.org/resource/5kya-mfst.json')

#Let's check the response is OK (return code 200)
if(response.status_code == 200):
    #We will convert the response to json 
    tallBuildings = response.json()\

   #someBldg = tallBuildings[0]
   #for key, value in someBldg.items():
   #    if 'polygon' in key:
   #        if 'coordinates' in someBldg['polygon']:
   #            print('coordinates found')
   #            for i in range(0,len(someBldg['polygon']['coordinates'][0])):
   #                print('\tLong ',i+1,':\t\t',someBldg['polygon']['coordinates'][0][i][0])
   #            for i in range(0,len(someBldg['polygon']['coordinates'][0])):
   #                print('\tLat  ',i+1,':\t\t',someBldg['polygon']['coordinates'][0][i][1])


#Excercise 1: Print to the screen the list of buildings 
#including relevant information about the building like structure type
#occupancy, number of stories, , total area.
for bldg in tallBuildings:
    printBldg(bldg)

#Excercise 2: Write the data from excercise 1 into a csv text file including latitude and longitude

#Exercise 3: Can we get PGA from USGS API for each building and include it in the output file
