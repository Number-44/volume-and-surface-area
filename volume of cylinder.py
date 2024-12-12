# Get user input for cylinder dimensions
height = float(input("Enter the height of the cylinder and press Enter: "))
radius = float(input("Enter the radius of the cylinder and press Enter: "))

# Display the input values
print("Height of the cylinder is: " + str(height))
print("Radius of the cylinder is: " + str(radius))

# Define the value of pi
pi = 3.14

# Calculate volume and surface area
volume = pi * radius**2 * height
surface_area = 2 * pi * height * radius + 2 * pi * radius**2

# Display the results
print("Volume of the cylinder is: " + str(volume))
print("Surface area of the cylinder is: " + str(surface_area))
