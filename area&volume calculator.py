# Calculate area and volume of a rectangle
length = int(input("Enter the length of a rectangle"))
breadth = int(input("Enter the breadth of a rectangle"))
height = int(input("Enter the height of a rectangle"))

area = length * breadth
volume = length * breadth * height
print(f"Area of the rectangle with length as {length} cm and breadth as {breadth} cm is {area} cm^2")
print(f"Volume of the rectangle with length as {length} cm and breadth as {breadth} cm is {volume} cm^3")
