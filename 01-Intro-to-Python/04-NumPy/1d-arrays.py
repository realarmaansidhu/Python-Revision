# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# Define height_in (example data)
height_in = [65, 70, 75, 80, 85, 90, 95, 100]

# Define weight_lb (example data, same length as height_in)
weight_lb = [150, 160, 170, 180, 190, 200, 210, 220]

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)

# Create a numpy array from weight_lb: np_weight_lb
np_weight_lb = np.array(weight_lb)

# Print out the weight at index 5
print(np_weight_lb[5])

# Print out sub-array of np_height_in: index 2 up to and including index 5
print(np_height_in[2:6])