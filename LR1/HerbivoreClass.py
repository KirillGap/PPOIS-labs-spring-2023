from WorldClass import Animal


class Herbivore(Animal):
    max_age = 25

    def __init__(self, _x, _y):
        super().__init__(_x, _y)

    def __str__(self):
        if self.gender == 'male':
            return 'O'
        else:
            return 'o'
