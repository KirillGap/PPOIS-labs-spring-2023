from WorldClass import Animal


class Predator(Animal):
    max_age = 15

    def __init__(self, _x, _y):
        super().__init__(_x, _y)

    def __str__(self):
        if self.gender == 'male':
            return 'X'
        else:
            return 'x'
