import math

radius = float(input("Please enter the radius of circle and this program will let you know the diameter, area, circumference of the circle:\n:"))
diameter = radius * 2
radius_square = pow(radius,2)
area = math.pi * radius_square
area = round(area, 3)
circumference = 2 * math.pi * radius
circumference = round(circumference, 3)
print(f"Diameter of the circle is {diameter}")
print(f"Area of Circle is {area}")
print(f"Circumference of circle is {circumference}")