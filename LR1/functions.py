import WorldClass
from WorldClass import *


def is_in_borders(_x, _y):
    return 0 <= _x <= 6 and 0 <= _y <= 49


def find_eat(_unit, _world):

    if isinstance(_unit, WorldClass.Herbivore):
        for i in range(_unit.coord_x - 3, _unit.coord_y + 4):
            for j in range(_unit.coord_y - 3, _unit.coord_y + 4):
                if is_in_borders(i, j) and isinstance(_world[i][j], WorldClass.Plant):
                    return i, j
        else:
            return None, None

    elif isinstance(_unit, WorldClass.Predator):
        for i in range(_unit.coord_x - 3, _unit.coord_y + 4):
            for j in range(_unit.coord_y - 3, _unit.coord_y + 4):
                if is_in_borders(i, j) and isinstance(_world[i][j], WorldClass.Herbivore):
                    return i, j
        else:
            return None, None


def settle_down(_x, _y, _world):
    for i in range(_x - 1, _x + 2):
        for j in range(_y - 1, _y + 2):
            if is_in_borders(i, j) and (_world[i][j] is None or isinstance(_world[i][j], WorldClass.Plant)):
                return i, j

    return None, None


def find_partner(_unit, _world, _gender):

    for i in range(_unit.coord_x - 3, _unit.coord_x + 4):
        for j in range(_unit.coord_y - 3, _unit.coord_y + 4):
            if is_in_borders(i, j) and type(_unit) is type(_world[i][j]):
                if _world[i][j].gender != _gender and _world[i][j].age >= 10 and _world[i][j].is_ready:
                    return i, j

    return None, None
