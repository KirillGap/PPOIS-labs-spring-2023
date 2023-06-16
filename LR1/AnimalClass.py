import WorldClass
from UnitClass import Unit as u
from random import randint
from functions import settle_down, find_eat, find_partner


class Animal(u):
    is_ready = True
    gender = ''
    hunger = 0

    def __init__(self, _x, _y):
        super().__init__(_x, _y)
        gender = randint(0, 1)
        if gender == 0:
            self.gender = 'male'
        else:
            self.gender = 'female'

    def reduce_hunger(self, _hunger):
        self.hunger += _hunger

    def rand_move(self, world_map):
        new_x, new_y = randint(self.coord_x - 2, self.coord_x + 2), randint(self.coord_y - 2, self.coord_y + 2)
        self.move(new_x, new_y, world_map)

    def move(self, _x_mark, _y_mark, world_map):
        new_x, new_y = settle_down(_x_mark, _y_mark, world_map)
        if new_x is not None:
            world_map[self.coord_x][self.coord_y] = None
            self.set_coords(new_x, new_y)
            world_map[new_x][new_y] = self

    def eat(self, world_map):
        food_x, food_y = find_eat(self, world_map)
        if food_x is not None:
            self.move(food_x, food_y, world_map)
            self_hunger = self.hunger
            food_hp = world_map[food_x][food_y].get_hp()
            world_map[food_x][food_y].reduce_hp(self_hunger)
            self.hunger = 0 if food_hp >= self.hunger else self.hunger - food_hp

        self.reduce_hunger(15)

    def reproduction(self, world_map):
        if self.age >= 10 and self.age % 5 == 0 and self.is_ready:
            partner_x, partner_y = find_partner(self, world_map, self.gender)
            if partner_x is not None:
                self.move(partner_x, partner_y, world_map)
                child_x, child_y = settle_down(self.coord_x, self.coord_y, world_map)
                if child_x is not None:
                    if isinstance(self, WorldClass.Predator):
                        child = WorldClass.Predator(child_x, child_y)
                    elif isinstance(self, WorldClass.Herbivore):
                        child = WorldClass.Herbivore(child_x, child_y)
                    world_map[child_x][child_y] = child
                    self.is_ready = False
