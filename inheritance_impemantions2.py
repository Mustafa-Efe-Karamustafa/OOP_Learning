import math

class Geometry:
    def __init__(self):
        self.total_edges = 0

    def calculate_area(self):
        pass

    def total_of_interior_angele(self):
        pass

class Triangle(Geometry):
    def __init__(self):
        super().__init__()
        self.length = 0
        self.height = 0
        self.total_edges = 3

    def calculate_area(self):
        return (self.length * self.height) / 2

    def total_of_interior_angele(self):
        interior_angele = 180 - (360 / self.total_edges)
        return self.total_edges * interior_angele


class Square(Geometry):
    def __init__(self):
        super().__init__()
        self.length = 0
        self.total_edges = 4

    def calculate_area(self):
        return self.length ** 2

    def total_of_interior_angele(self):
        interior_angele = 180 - (360 / self.total_edges)
        return self.total_edges * interior_angele

class Circle(Geometry):
    def __init__(self):
        super().__init__()
        self.radius = 0

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Besgen(Geometry):
    def __init__(self):
        super().__init__()
        self.total_edges = 5

    def total_of_interior_angele(self):
        interior_angele = 180 - (360 / self.total_edges)
        return self.total_edges * interior_angele

    def calculate_interior_angle(self):
        return (self.total_edges - 2) * 180

t0 = Triangle()
s0 = Square()
c0 = Circle()

t0.length = 10
t0.height = 5

s0.length = 10


c0.radius = 5

b0 = Besgen()


print(t0.calculate_area())
print(s0.calculate_area())
print(c0.calculate_area())
print("-----------------------")
print("iç açılar toplamı",t0.total_of_interior_angele())
print("iç açılar toplamı",s0.total_of_interior_angele())
print("iç açılar toplamı besgen",b0.total_of_interior_angele())
print(b0.calculate_interior_angle())
print(math.pi)

my_list = [t0,s0,c0,b0]
for i in my_list:
    print(type(i),"",i.calculate_area())