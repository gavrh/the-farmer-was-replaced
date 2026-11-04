# move module
# ways to get around

# pylint: disable=not-an-iterable
# pylint: disable=invalid-sequence-index
from __builtins__ import *

def to(x: int, y: int):
    d_x: int = get_pos_x()
    d_y: int = get_pos_y()

    while (d_x != x) or (d_y != y):
        if d_x < x:
            move(East)
            d_x += 1
        elif d_x > x:
            move(West)
            d_x -= 1

        if d_y < y:
            move(North)
            d_y += 1
        elif d_y > y:
            move(South)
            d_y -= 1
