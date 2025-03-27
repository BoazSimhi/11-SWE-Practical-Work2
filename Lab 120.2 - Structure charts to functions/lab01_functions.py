from math import pi

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return str(length * width) + " units\u00b2"

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return str(radius ** 2) + "π" + " units\u00b2"

# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    return str(base * height / 2) + " units\u00b2"

def calculate_cube_volume(side):
    return str(side ** 3) + " units\u00b3"

def calculate_cylinder_volume(radius, height):
    return str(height * (radius ** 2)) + "π" + " units\u00b3"

def calculate_sphere_volume(radius):
    return str(4 * (radius ** 3) / 3) + "π" + " units\u00b3"

# Menu function to allow user selection
def menu():
    print("Choose a calculation:")
    print("1. Area of Rectangle")
    print("2. Area of Circle")
    print("3. Area of Triangle")
    print("4. Volume of Cube")
    print("5. Volume of Cylinder")
    print("6. Volume of Sphere")

# Main logic to get user input and call the appropriate function
menu()
choice = int(input("Enter your choice: "))

if choice == 1:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area:", calculate_rectangle_area(length, width))
elif choice == 2:
    radius = float(input("Enter radius: "))
    print("Area:", calculate_circle_area(radius))
elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area:", calculate_triangle_area(base, height))
elif choice == 4:
    side = float(input("Enter side length: "))
    print("Volume:", calculate_cube_volume(side))
elif choice == 5:
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))
    print("Volume:", calculate_cylinder_volume(radius, height))
elif choice == 6:
    radius = float(input("Enter radius: "))
    print("Volume:", calculate_sphere_volume(radius))
else:
    print("Invalid choice!")
