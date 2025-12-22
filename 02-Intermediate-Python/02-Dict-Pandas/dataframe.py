# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country': names,
    'drives_right': dr,
    'cars_per_cap': cpc
}

# # Build a DataFrame cars from my_dict: cars
# cars = pd.DataFrame(my_dict)

# # # Print cars
# # print(cars)

# # Build cars DataFrame
# cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
# cars = pd.DataFrame(cars_dict)

# # Definition of row_labels
# row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# # Specify row labels of cars
# cars.index = row_labels

# # Print cars again
# print(cars)

my_cars = {'cars_per_cap': {'US': 809, 'AUS': 731, 'JPN': 588, 'IN': 18, 'RU': 200, 'MOR': 70, 'EG': 45}, 'country': {'US': 'United States', 'AUS': 'Australia', 'JPN': 'Japan', 'IN': 'India', 'RU': 'Russia', 'MOR': 'Morocco', 'EG': 'Egypt'}, 'drives_right': {'US': True, 'AUS': False, 'JPN': False, 'IN': False, 'RU': True, 'MOR': True, 'EG': True}}

cars = pd.DataFrame(my_cars)
print(cars)

# Print out country column as Pandas Series
print(cars["country"])

# Print out country column as Pandas DataFrame
print(cars[["country"]])

# Print out DataFrame with country and drives_right columns
print(cars[["country", "drives_right"]])

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Print out observation for Japan
print(cars.loc["JPN"])

# Print out observations for Australia and Egypt
print(cars.loc[["AUS", "EG"]])

# Print out drives_right value of Morocco
print(cars.loc[["MOR"], ["drives_right"]])

# Print sub-DataFrame
print(cars.loc[["RU", "MOR"], ["country", "drives_right"]])

# Print out drives_right column as Series
print(cars["drives_right"])

# Print out drives_right column as DataFrame
print(cars[["drives_right"]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ["cars_per_cap", "drives_right"]])