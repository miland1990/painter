from dataclasses import dataclass, field
from typing import Any, Optional, Union, AnyStr, Any, List
from abc import ABC
import re
import itertools

from constants import CANVAS_HORIZONTAL_SIGN, CANVAS_VERTICAL_SIGN, FILL_SIGN, PSEUDO_SIGN

from business import Painter, Point, Canvas, Line, Rectangle


def convert_to_rectangle(x1, y1, x2, y2):
    return Rectangle(
        left_upper_point=Point(x=x1, y=y1, value=PSEUDO_SIGN),
        right_upper_point=Point(x=x2, y=y1, value=PSEUDO_SIGN),
        left_inferior_point=Point(x=x1, y=y2, value=PSEUDO_SIGN),
        right_inferior_point=Point(x=x2, y=y2, value=PSEUDO_SIGN)
    )


def convert_to_line(x1, y1, x2, y2):
    return Line(
        start=Point(x=x1, y=y1, value=PSEUDO_SIGN),
        end=Point(x=x2, y=y2, value=PSEUDO_SIGN)
    )


def create_new_canvas(width, height):
    return Canvas(
        left_upper_point=Point(x=0, y=0),
        right_upper_point=Point(x=width+1, y=0),
        left_inferior_point=Point(x=0, y=height),
        right_inferior_point=Point(x=width+1, y=height+1),
    )


def convert_to_canvas(content):
    canvas = dict()
    for y, line in enumerate(content):
        for x, symbol in enumerate(line):
            if symbol != '\n':
                point = Point(x=x, y=y, value=' ')
                canvas[point.key] = point.value


def convert_from_canvas(painter: Painter) -> List[AnyStr]:
    strings = []
    for y in range(painter.canvas.left_inferior_point.x, painter.canvas.right_inferior_point.y + 1):
        exact_string = []
        for x in range(painter.canvas.left_upper_point.x, painter.canvas.right_upper_point.x + 1):
            exact_string.append(painter.picture[Point(x=x, y=y).key])
        strings.append(''.join(exact_string))
    return '\n'.join(strings)
