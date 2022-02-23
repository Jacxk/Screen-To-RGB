from math import ceil
from random import randrange
from typing import List

def fade_between(cfrom=[0,0,0], cto=None) -> List[List]:
    colors = []
    if not cto:
        cto = [randrange(0, 255), randrange(0, 255), randrange(0, 255)]

    while not _color_reached(cfrom, cto):
        for i in range(3):
            if cfrom[i] > cto[i]:
                cfrom[i] -= 10
               
            if cfrom[i] < cto[i]:
                cfrom[i] += 10
 
            colors.append(list(cfrom))
  
    return colors

def _color_reached(cfrom, cto) -> bool:
    r1, g1, b1 = cfrom
    r2, g2, b2 = cto

    c1 = r2-10 <= r1 <= r2+10
    c2 = g2-10 <= g1 <= g2+10
    c3 = b2-10 <= b1 <= b2+10

    return c1 and c2 and c3