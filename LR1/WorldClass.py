from Exceptions import PopulatedCellException
from AnimalClass import Animal
from HerbivoreClass import Herbivore
from PredatorClass import Predator
from PlantClass import Plant


class World:
    forest = []

    def __init__(self, map=None):
        if map is None:
            map = []
            for _ in range(10):
                lst = [None] * 50
                map.append(lst)
        self.forest = map

    def show(self):
        for x in range(7):
            line = ""
            for y in range(50):
                line += str(self.forest[x][y]) if self.forest[x][y] is not None else '.'
            print(line)

    def add(self, _x, _y, _type):
        if self.forest[_x][_y] is None:

            if _type == 'хищник':
                predator = Predator(_x, _y)
                self.forest[_x][_y] = predator

            elif _type == 'травоядное':
                herb = Herbivore(_x, _y)
                self.forest[_x][_y] = herb

            elif _type == 'растение':
                plant = Plant(_x, _y)
                self.forest[_x][_y] = plant

        else:
            if isinstance(self.forest[_x][_y], Herbivore):
                raise PopulatedCellException("Herbivore here already!")
            elif isinstance(self.forest[_x][_y], Plant):
                raise PopulatedCellException("Plant here already!")
            elif isinstance(self.forest[_x][_y], Predator):
                raise PopulatedCellException("Predator here already!")
            else:
                raise PopulatedCellException("Unknown error!")

    def tick(self):
        for line in self.forest:
            for unit in line:
                if unit is not None and not unit.is_moved:
                    unit.life(self.forest)
                    unit.is_moved = True

        for i in range(len(self.forest)):
            for j in range(len(self.forest[0])):
                if self.forest[i][j] is not None:
                    self.forest[i][j].is_moved = False
                    if self.forest[i][j].age >= self.forest[i][j].max_age:
                        self.forest[i][j] = None
                    elif self.forest[i][j].hp <= 0:
                        self.forest[i][j] = None
                    elif (isinstance(self.forest[i][j], Predator) or isinstance(self.forest[i][j], Herbivore)) and self.forest[i][j].hunger >= 100:
                        self.forest[i][j] = None
