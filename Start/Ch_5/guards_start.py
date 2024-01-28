# Example file for Advanced Python: Language Features by Joe Marini
# Using pattern guards to restrict how matches are made

# define some geometric shapes
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        return 3.14 * (self.radius ** 2)


class Square:
    def __init__(self, side):
        self.side = side

    def getarea(self):
        return self.side * self.side


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height


# create a list of some shapes
shapes = [Circle(5), Square(4), Rectangle(4, 6),
          Square(7), Circle(9), Rectangle(2, 5), Rectangle(3,3)]

# use pattern matching to process each shape
# include pattern guards for more detailed processing
for shape in shapes:
    match shape:
        # add a pattern guard for Circle
        case Circle(radius=r) if r >= 6:
            print(f"LARGE Circle with area {shape.getarea()}")
        case Circle():
            print(f"Circle with area {shape.getarea()}")
        case Square():
            print(f"Square with area {shape.getarea()}")
        case Rectangle(width=w, height=h) if w == h:
            print(f"SQUARE Rectangle with area {shape.getarea()}")
        case Rectangle():
            print(f"Rectangle with area {shape.getarea()}")
        case _:
            print(f"Unrecognized shape: {type(shape)}")

# Pattern guards can get fairly sophisticated
dataset = ["UPPER", 5, "Mixed Case", True, None]
for d in dataset:
    match d:
        case str() as s if s.isupper():
            print(f"found upper {d}")
        case str():
            print(f"not upper {d}")
        case bool():
            print(f"A boolean {d}")
        case int():
            print(f"An int {d}")
        case _:
            print(f"{d}: Something else")
my_list = [2,4,6,7,8,10,None,"hello"]
for n in my_list:
    match n:
        case int() as n if n % 2 == 0:
            print(f"Found even: {n}")
        case int() as n if n % 2 != 0:
            print(f"Found odd: {n}")
        case _:
            print(f"Invalid input: {n}")
            