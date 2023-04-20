from math import pi  # для числа пи
import random as rnd  # для генерации


# для проверки типов переданных переменных
def check_types(*types):
    def level1(func):
        def level2(*args, **kwargs):
            for i in args[1:]:
                if type(i) not in types:
                    raise TypeError(f"Args must be some of types {types}")
            result = func(*args, **kwargs)
            return result

        return level2

    return level1


class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):

    @check_types(float, int)
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return pi * self.__radius ** 2

    def info(self):
        print(f"Circle "
              f"radius: {self.__radius:.2f} {self.unit}, "
              f"area: {self.calculate_area():.2f} {self.unit}")


class RightTriangle(Figure):

    @check_types(float, int)
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return self.__side_b * self.__side_a / 2

    def info(self):
        print(f"RightTriangle "
              f"side_a: {self.__side_a:.2f} {self.unit}, "
              f"side_b: {self.__side_b:.2f} {self.unit}, "
              f"area: {self.calculate_area():.2f} {self.unit}")


figures = [Circle(rnd.uniform(1, 30)) for i in range(2)]
figures += [RightTriangle(rnd.uniform(1, 30), rnd.uniform(1, 30)) for i in range(3)]

for i in figures:
    i.info()
