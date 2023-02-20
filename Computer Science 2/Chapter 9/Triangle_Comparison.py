class Triangle:
    def __init__(shape):
        shape.base = None
        shape.height = None

    def set_shape_base(shape, int):
        shape.base = int
    
    def set_shape_height(shape, int):
        shape.height = int
    
    def compare_shape_areas(shape_one, shape_two):
        area_of_shape_one = shape_one.base * shape_one.height / 2
        area_of_shape_two = shape_two.base * shape_two.height / 2
        if area_of_shape_one > area_of_shape_two:
            print("Shape one is larger in area")
        else:
            print("Shape two is larger in area")
    
triangle1 = Triangle()
triangle2 = Triangle()

triangle1.set_shape_base(int(input("Enter the base length for triangle 1")))
triangle1.set_shape_height(int(input("Enter the height length for triangle 1")))
triangle2.set_shape_base(int(input("Enter the base length for triangle 2")))
triangle2.set_shape_height(int(input("Enter the height length for triangle 2")))

Triangle.compare_shape_areas(triangle1, triangle2)
