
def main():
	#Code Input and calling of Miles to Feet conversiton
	miles=2
	feet=miles_to_feet(miles)
	print(f"{miles} miles is {feet} feet")

	#Circumference of a circle
	radius=10
	print(f"{radius} gives {circle_circumference(radius):.2f} circumference.")

	#Trangle area using Heron's formula
	test_trangle_area(-2, 4, 1, 6, 2, 1)

	#powerball Game
	powerball()
	
	
#Function to convert miles to feet
def miles_to_feet(miles):
	return miles*5280

#Circumference of a circle
import math
def circle_circumference(radius):
	return 2*math.pi*radius

# Trangle area using Heron's Formula
def triangle_area(x0, y0, x1, y1, x2, y2):

	a = point_distance(x0, y0, x1, y1)
	b = point_distance(x0, y0, x2, y2)
	c = point_distance(x1, y1, x2, y2)
	
	s = (a + b + c) / 2
	
	return (s * (s - a) * (s - b) * (s - c)) ** 0.5
def point_distance(x0, y0, x1, y1):
	return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
	
def test_trangle_area(x0, y0, x1, y1, x2, y2):
	
	print ("A triangle with vertices (" + str(x0) + "," + str(y0) + "),", end="")
	print ("(" + str(x1) + "," + str(y1) + "), and", end="")
	print ("(" + str(x2) + "," + str(y2) + ") has an area of" ,end="")
	print (str(triangle_area(x0, y0, x1, y1, x2, y2)) + ".")


# Powerball function
# Student should enter function on the next lines.
import random
def powerball():
    """Prints Powerball lottery numbers."""
    
    print ("Today's numbers are " + str(random.randrange(1, 60)) + ",",end="")
    print (str(random.randrange(1, 60)) + ",",end="")
    print (str(random.randrange(1, 60)) + ",",end="")
    print (str(random.randrange(1, 60)) + ", and",end="")
    print (str(random.randrange(1, 60)) + ". The Powerball number is",)
    print (str(random.randrange(1, 36)) + ".")

main()