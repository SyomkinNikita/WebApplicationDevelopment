from OOP.Figure import Figure
import math

from OOP.FigureColor import FigureColor


class Circle(Figure):
    FIGURE_TYPE = "Circle"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, r_param):
        self.r = r_param
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def square(self):
        return math.pi * (self.r ** 2)

    def __repr__(self):
        return '{}{} цвета радиуса {} площадь {}.'.format(
            Circle.get_figure_type(), self.fc.colorproperty, self.r, self.square()
        )
