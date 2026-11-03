from __builtins__ import *


while True:
    x = 3
    i = 0
    while i < x:

        if can_harvest():
            harvest()

        till()
        move(North)
        i+=1
