from WorldClass import World
from Exceptions import PopulatedCellException
import pickle


def menu():
    w = World()
    while True:
        w.show()
        print("Команды:")
        print("(Добавить существо) добавить [x] [y] [травоядное/хищник/растение]")
        print("(Выйти без сохранения) выход")
        print("(Сохранить прогресс) сохранить [название]")
        print("(Загрузить прогресс) загрузить [название]")
        command = input("Введите команду: \n")
        match command.split():
            case["добавить", x, y, unit_type]:
                try:
                    w.add(int(x), int(y), unit_type)
                except PopulatedCellException as e:
                    print(e.message)

            case["сохранить", name]:
                name = 'saves/' + name
                with open(name, 'wb') as save:
                    pickle.dump(w.forest, save)
                    # name = 'saves/' + name + '.txt'

            case["загрузить", name]:
                name = 'saves/' + name
                with open(name, 'rb') as save:
                    w = World(pickle.load(save))

            case["выход"]:
                return

        w.tick()


menu()
