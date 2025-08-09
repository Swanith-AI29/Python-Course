def square(side):
    area = side * side
    perimeter = 4 * side
    return area, perimeter

def rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


print("Welcome to the Area and Perimeter Calculator!")
shape = input("Enter the shape (square/rectangle): ")

if shape == "square":
    side = float(input("Enter the side length of the square: "))
    area, perimeter = square(side)
    print(f"Area of the square: {area}")
    print(f"Perimeter of the square: {perimeter}")

elif shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area, perimeter = rectangle(length, width)
    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")

else:
    print("Invalid shape entered. ")
