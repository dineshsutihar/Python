radius, side = input("Enter radius of circle and side of square separated by a space: ").split()

# Converting the inputs from string to float
radius = float(radius)
side = float(side)

# Calculating area of the circle and the square
area_circle = 3.14159 * radius ** 2
area_square = side ** 2

# Displaying the results
print("Area of circle: {:.2f}".format(area_circle))
print("Area of square: {:.2f}".format(area_square))