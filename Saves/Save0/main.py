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
    Entities.Sunflower,
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

tilled_crops = {
    Entities.Bush,
    Entities.Carrot,
    Entities.Pumpkin,
    Entities.Sunflower
}

def main():
    crop = Entities.Grass

    while True:
        y: int = get_pos_y()

        if y == 0:
            move(East)

        if len(crop_list) > y:
            crop = crop_list[y]
        else:
            crop = Entities.Grass

        should_be_tilled = crop in tilled_crops
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
