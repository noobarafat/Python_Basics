import math

def circle_area(radius):
    return math.pi * radius**2

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def calculate_area():
    print("Choose a shape to calculate the area:")
    print("1. Circle\n2. Rectangle\n3. Triangle")
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
        print("Area of the circle:", area)
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(length, width)
        print("Area of the rectangle:", area)
    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = triangle_area(base, height)
        print("Area of the triangle:", area)
    else:
        print("Invalid choice!")

calculate_area()
