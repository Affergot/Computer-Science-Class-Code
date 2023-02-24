import time
from TypedOut import *
class Triangle:
    def __init__(shape):
        shape.base = None
        shape.height = None

    def set_shape_base(shape, int):
        shape.base = int
    
    def set_shape_height(shape, int):
        shape.height = int
    
    def get_triangle_area(shape):
        return shape.base * shape.height / 2
    
if __name__ == "__main__":
    
    triangle1 = Triangle()
    triangle2 = Triangle()
    charByChar("Enter the base and height of two triangles to compare their areas\n")
    time.sleep(1)
    charByChar("Enter the base length for first Triangle\n")
    triangle1.set_shape_base(int(input(":")))

    charByChar("Enter the height length for the first Triangle\n")
    triangle1.set_shape_height(int(input(":")))

    charByChar("Enter the base length for the second Triangle\n")
    triangle2.set_shape_base(int(input(":")))

    charByChar("Enter the height length for the second Triangle\n")
    triangle2.set_shape_height(int(input(":")))

    triangle1_area = triangle1.get_triangle_area()
    triangle2_area = triangle2.get_triangle_area()

    area_difference = triangle1_area - triangle2_area
    if area_difference == 0:
        charByChar("The two triangles have the same area.")
    if area_difference > 0:
        charByChar(f"The first triangle is {area_difference} units larger than the second triangle with a total area of {triangle1_area}.")
    elif area_difference < 0:
        charByChar(f"The second triangle is {abs(area_difference)} units larger than the first triangle with a total area of {triangle2_area}.")
    time.sleep(1)

    charByChar("\nTriangle with smaller area:\n")
    print("Base:", triangle1.base if triangle1_area < triangle2_area else triangle2.base)
    time.sleep(1)
    print("Height:", triangle1.height if triangle1_area < triangle2_area else triangle2.height)
    time.sleep(1)
    print("Area:", triangle1_area if triangle1_area < triangle2_area else triangle2_area)
