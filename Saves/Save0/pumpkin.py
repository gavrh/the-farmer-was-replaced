# pumpkin module

# pylint: disable=not-an-iterable
# pylint: disable=invalid-sequence-index
from __builtins__ import *
import mv

# 6x6 pumpkin patch
def pumpkin_patch(
    patch: tuple[dict[int, tuple[tuple[int, int], tuple[int, int]]], bool],
    size: int,
    start_x: int,
    start_y: int
):
    if not patch[1]:
        init_patch(patch, size, start_x, start_y)

    mv.to(start_x, start_x)


def init_patch(patch: list[tuple[int, int]], size: int, start_x: int, start_y: int):
    for x in range(size):
        for y in range(size):
            patch.append((start_x + x, start_y + y))
