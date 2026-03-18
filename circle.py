class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = float(radius)

    def perimeter(self):
        p = 2* self.pi * self.radius
        return f'Circumfernace is {p}'

    def area(self):
        a = self.pi * (self.radius **2)
        return f'Area is {a}'




