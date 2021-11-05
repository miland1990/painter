from dataclasses import dataclass, field
from typing import Optional, Union, AnyStr, List

from constants import CANVAS_HORIZONTAL_SIGN, CANVAS_VERTICAL_SIGN, FILL_SIGN, PSEUDO_SIGN


@dataclass(order=True)
class Point:
    x: int
    y: int
    value: Optional[AnyStr]=None

    def __hash__(self):
        return int('{}000{}'.format(self.x, self.y))

    @property
    def key(self):
        return self.__hash__()


@dataclass(order=True)
class Line:
    start: Point
    end: Point

    @property
    def space(self):
        return []

    @property
    def points(self):
        for x in range(self.start.x, self.end.x + 1):
            for y in range(self.start.y, self.end.y + 1):
                yield Point(x=x, y=y, value=PSEUDO_SIGN)

    def __hash__(self):
        return int('{}000{}000{}000{}'.format(
            self.start.x, self.start.y, self.end.x, self.end.y)
        )


@dataclass(order=True)
class Rectangle:
    left_upper_point: Point
    right_upper_point: Point
    left_inferior_point: Point
    right_inferior_point: Point

    @property
    def space(self):
        return Rectangle(
            left_upper_point=Point(x=self.left_upper_point.x + 1, y=self.left_upper_point.y + 1, value=' '),
            right_upper_point=Point(x=self.right_upper_point.x - 1, y=self.right_upper_point.y + 1, value=' '),
            left_inferior_point=Point(x=self.left_inferior_point.x + 1, y=self.left_inferior_point.y - 1, value=' '),
            right_inferior_point=Point(x=self.right_inferior_point.x - 1, y=self.right_inferior_point.y - 1, value=' ')
        )

    @property
    def points(self):
        for x in range(self.left_upper_point.x, self.right_upper_point.x + 1):
            for y in range(self.left_upper_point.y, self.left_inferior_point.y + 1):
                if y in (self.left_upper_point.y, self.right_inferior_point.y):
                    yield Point(x=x, y=y, value=PSEUDO_SIGN)
                elif x in (self.left_upper_point.x, self.right_upper_point.x):
                    yield Point(x=x, y=y, value=PSEUDO_SIGN)

    def __hash__(self):
        return int('{}000{}000{}000{}'.format(
            self.left_upper_point.x, self.left_upper_point.y, self.right_inferior_point.x, self.right_inferior_point.y)
        )


class Canvas(Rectangle):

    @property
    def points(self):
        for x in range(self.left_upper_point.x, self.right_upper_point.x + 1):
            for y in range(self.left_upper_point.y, self.right_inferior_point.y + 1):
                if y in (self.left_upper_point.y, self.right_inferior_point.y):
                    value = CANVAS_HORIZONTAL_SIGN
                    yield Point(x=x, y=y, value=value)
                else:
                    value = CANVAS_VERTICAL_SIGN
                    yield Point(x=x, y=y, value=value)
        for x in range(self.space.left_upper_point.x, self.space.right_upper_point.x + 1):
            for y in range(self.space.left_upper_point.y, self.space.right_inferior_point.y + 1):
                yield Point(x=x, y=y, value=' ')


class Painter:

    def __init__(self, sign: Optional[AnyStr] = PSEUDO_SIGN) -> None:
        self.sign = sign
        self.picture = dict()
        self.canvas = None

    def start_new_picture(self, canvas: Canvas) -> None:
        self.canvas = canvas
        self.picture = {point.key: point.value for point in canvas.points}

    def change_brash(self, sign):
        self.sign = sign

    def paint_figure(self, figure: Union[Rectangle, Line]) -> None:
        for point in figure.points:
            self.picture[point.key] = self.sign

    def fill_with_colour(self, colour: AnyStr) -> None:
        pass
        # 1) в self.picture найти точки, у которых рядом есть еще "x","|","-"
        # 2) выбрать одно направление движения 
        # 3) пытаться прийти в изначальную точку и запомнить углы прямоугольников либо найти конец линии
        # 4) полученные прямоугольники разложить на точки и внести их в дикт исключений
        # 5) проитерироваться по всем точкам картины и закрасить цветом те, что не в исключениях 
