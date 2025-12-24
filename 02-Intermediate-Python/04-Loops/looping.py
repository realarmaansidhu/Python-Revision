import numpy as np
import pandas as pd

# Initialize offset
offset = 8

# Code the while loop
while(offset!=0):
    print("correcting...")
    offset = offset - 1
    print(offset)

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if (offset > 0) :
      offset = offset - 1
    else : 
      offset = offset + 1    
    print(offset)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas:
    print(area)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for area_index, area in enumerate(areas):
    print("room " + str(area_index) + ": " + str(area))

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for room in house:
    print("the " + room[0] + " is " + str(room[1]) + " sqm")

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for k, v in europe.items():
    print("the capital of " + k + " is " + v)

# Import numpy as np
import numpy as np

np_height = np.array([74, 74, 72, 73, 75, 75, 73])

np_baseball = np.array([[ 74, 180],
 [ 74, 215],
 [ 72, 210],
 [ 75, 205],
 [ 75, 190],
 [ 73, 195]])

# For loop over np_height
for e in np_height:
    print(str(e) + " inches")

# For loop over np_baseball
for i in np.nditer(np_baseball):
    print(i)

cars = {'cars_per_cap': {'US': 809, 'AUS': 731, 'JPN': 588, 'IN': 18, 'RU': 200, 'MOR': 70, 'EG': 45}, 'country': {'US': 'United States', 'AUS': 'Australia', 'JPN': 'Japan', 'IN': 'India', 'RU': 'Russia', 'MOR': 'Morocco', 'EG': 'Egypt'}, 'drives_right': {'US': True, 'AUS': False, 'JPN': False, 'IN': False, 'RU': True, 'MOR': True, 'EG': True}}

cars = pd.DataFrame(cars)

# Iterate over rows of cars
for label, row in cars.iterrows():
    print(label)
    print(row)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row["cars_per_cap"]))

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
     cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)