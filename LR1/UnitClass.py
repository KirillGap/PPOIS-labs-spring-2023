from abc import ABC

import AnimalClass


class Unit(ABC):
    is_moved = True
    age = 0
    max_age = 0
    coord_x = -1
    coord_y = -1
    hp = 100

    def __del__(self):
        pass

    def __init__(self, _x, _y):
        self.set_coords(_x, _y)

    def get_hp(self):
        return self.hp

    def set_coords(self, _x, _y):
        self.coord_x = _x
        self.coord_y = _y

    def reduce_hp(self, _damage):
        self.hp -= _damage

    def aging(self):
        self.age += 1

    # @abstractmethod
    def reproduction(self, world_map):
        pass

    def life(self, _world_map):
        if isinstance(self, AnimalClass.Animal):
            self.eat(_world_map)
            self.rand_move(_world_map)
        self.reproduction(_world_map)
        self.aging()
