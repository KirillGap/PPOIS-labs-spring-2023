from UnitClass import Unit
from functions import is_in_borders

class Plant(Unit):
    hp = 30
    max_age = 50

    def __init__(self, _x, _y):
        super().__init__(_x, _y)

    def heal(self):
        self.hp += 5

    def __str__(self):
        return '*'

    def reproduction(self, world_map):
        if self.age >= 10 and self.age % 10 == 0:
            if is_in_borders(self.coord_x + 1, self.coord_y) and world_map[self.coord_x + 1][self.coord_y] is None:
                world_map[self.coord_x + 1][self.coord_y] = Plant(self.coord_x + 1, self.coord_y)

            if is_in_borders(self.coord_x - 1, self.coord_y) and world_map[self.coord_x - 1][self.coord_y] is None:
                world_map[self.coord_x - 1][self.coord_y] = Plant(self.coord_x - 1, self.coord_y)

            if is_in_borders(self.coord_x, self.coord_y + 1) and world_map[self.coord_x][self.coord_y + 1] is None:
                world_map[self.coord_x][self.coord_y + 1] = Plant(self.coord_x, self.coord_y + 1)

            if is_in_borders(self.coord_x, self.coord_y - 1) and world_map[self.coord_x][self.coord_y - 1] is None:
                world_map[self.coord_x][self.coord_y - 1] = Plant(self.coord_x, self.coord_y - 1)
