# pylint: disable=not-an-iterable
# pylint: disable=invalid-sequence-index
from __builtins__ import *
import mv
import pumpkin
import sunflower

crop_list = [
    Entities.Tree,
    Entities.Carrot,
    Entities.Carrot,
    Entities.Carrot,
    Entities.Pumpkin,
    Entities.Pumpkin,
    Entities.Pumpkin,
    Entities.Pumpkin,
    Entities.Pumpkin,
    Entities.Grass,
    Entities.Grass,
    Entities.Grass,
]

specific_list = [
    Entities.Carrot,
    Entities.Carrot,
    Entities.Carrot,
    Entities.Carrot,
    Entities.Carrot,
    Entities.Carrot,
    Entities.Carrot,
    Entities.Carrot,
]

def main():
    crop = Entities.Grass

    while True:
        y: int = get_pos_y()

        if y == 0:
            move(East)

        crop = crop_list[y]

        should_be_tilled = crop in (Entities.Bush, Entities.Carrot, Entities.Pumpkin)
        should_be_watered = False # crop == Entities.Tree

        if should_be_tilled and get_ground_type() != Grounds.Soil:
            till()
        elif not should_be_tilled and get_ground_type() == Grounds.Soil:
            till()

        if can_harvest():
            if harvest():
                if plant(crop):
                    if should_be_watered:
                        use_item(Items.Water)

        else:
            if plant(crop):
                if should_be_watered:
                    use_item(Items.Water)

        move(North)


main()
