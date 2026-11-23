
import random

MAZE = [
    ".......",
    ".###.#.",
    "...#.#.",
    "##.#...",
    "...#.#.",
    ".#.....",
    "......."
]

EXIT = (6, 6)


class Player:
    def __init__(self):
        self.name = input("Введите имя: ")
        self.health = 100
        self.x = 0
        self.y = 0
        self.inventory = []

    def move(self, direction):
        x = self.x
        y = self.y

        if direction == "вверх":
            y -= 1
        elif direction == "вниз":
            y += 1
        elif direction == "влево":
            x -= 1
        elif direction == "вправо":
            x += 1
        else:
            print("Неверное направление.")
            return False

        if x < 0 or x >= 7 or y < 0 or y >= 7:
            print("Нельзя выйти за границы.")
            return False

        if MAZE[y][x] == "#":
            print("Здесь стена!")
            return False

        self.x = x
        self.y = y
        return True


class Room:
    def __init__(self, name, room_type, items=None):
        self.name = name
        self.type = room_type
        self.items = list(items) if items else []


def create_rooms():
    rooms = {
        (2, 0): Room("Комната с предметами", "предметы",
                     ["Зелье", "Меч", "Монета"]),
        (4, 2): Room("Комната с монстром", "монстр"),
        (2, 4): Room("Комната с ловушкой", "ловушка"),
        (6, 3): Room("Комната с порталом", "портал")
    }
    return rooms


def show_map(player, rooms):
    print("\nКарта лабиринта:")

    for y in range(7):
        line = ""

        for x in range(7):
            point = (x, y)

            if point == (player.x, player.y):
                symbol = "P"
            elif point == EXIT:
                symbol = "E"
            elif MAZE[y][x] == "#":
                symbol = "#"
            elif point in rooms:
                room = rooms[point]

                if room.type == "предметы":
                    symbol = "I"
                elif room.type == "монстр":
                    symbol = "M"
                elif room.type == "ловушка":
                    symbol = "T"
                elif room.type == "портал":
                    symbol = "O"
                else:
                    symbol = "."
            else:
                symbol = "."

            line += symbol + " "

        print(line)


def inventory_management(player, room=None):
    while True:
        print("\nВаш инвентарь:", player.inventory)
        print("1 - Взять предметы")
        print("2 - Выбросить предмет")
        print("3 - Сортировать инвентарь")
        print("4 - Изменить порядок предметов")
        print("5 - Найти предмет")
        print("6 - Скопировать список")
        print("7 - Показать полезные предметы")
        print("8 - Использовать зелье")
        print("0 - Назад")

        action = input("Выберите действие: ")

        if action == "1":
            if room is None or not room.items:
                print("Нет предметов для сбора.")
            else:
                print("Предметы в комнате:", room.items)
                choice = input("Взять все или один? (все/один): ")

                if choice == "все":
                    player.inventory.extend(room.items)
                    room.items.clear()
                    room.type = "пустая"
                    print("Все предметы собраны.")

                elif choice == "один":
                    number = int(input("Номер предмета: "))

                    if 1 <= number <= len(room.items):
                        item = room.items.pop(number - 1)
                        player.inventory.append(item)
                        print("Вы взяли:", item)

                        if not room.items:
                            room.type = "пустая"
                    else:
                        print("Неверный номер.")

        elif action == "2":
            if player.inventory:
                choice = input("Введите номер или название: ")

                if choice.isdigit():
                    number = int(choice) - 1

                    if 0 <= number < len(player.inventory):
                        item = player.inventory.pop(number)
                        print("Вы выбросили:", item)
                    else:
                        print("Неверный номер.")

                elif choice in player.inventory:
                    player.inventory.remove(choice)
                    print("Предмет удалён.")
                else:
                    print("Такого предмета нет.")
            else:
                print("Инвентарь пуст.")

        elif action == "3":
            player.inventory.sort()
            print("Инвентарь отсортирован:", player.inventory)

        elif action == "4":
            player.inventory.reverse()
            print("Порядок изменён:", player.inventory)

        elif action == "5":
            item = input("Какой предмет ищем? ")

            if item in player.inventory:
                number = player.inventory.index(item) + 1
                print("Предмет найден. Номер:", number)
            else:
                print("Предмет не найден.")

        elif action == "6":
            copied = player.inventory.copy()

            print("Копия:", copied)
            print("Первые два предмета:", copied[:2])
            print("Остальные предметы:", copied[2:])

        elif action == "7":
            useful = [
                item for item in player.inventory
                if item == "Зелье" or item == "Меч"
            ]
            print("Полезные предметы:", useful)

        elif action == "8":
            if "Зелье" in player.inventory:
                player.inventory.remove("Зелье")
                player.health = min(100, player.health + 30)
                print("Здоровье восстановлено. HP:", player.health)
            else:
                print("У вас нет зелья.")

        elif action == "0":
            break

        else:
            print("Неверная команда.")


def interaction(player, room, rooms):
    print("\nВы вошли:", room.name)

    if room.type == "предметы":
        inventory_management(player, room)

    elif room.type == "монстр":
        if "Меч" in player.inventory:
            damage = 10
            print("Меч помог защититься от монстра!")
        else:
            damage = 30
            print("Монстр атаковал вас!")

        player.health = max(0, player.health - damage)
        print("Потеряно HP:", damage)
        room.type = "пустая"

    elif room.type == "ловушка":
        print("Вы попали в ловушку!")
        player.health = max(0, player.health - 20)
        print("Потеряно 20 HP.")
        room.type = "пустая"

    elif room.type == "портал":
        answer = input("Использовать портал? (да/нет): ")

        if answer == "да":
            free_cells = [
                (x, y)
                for y in range(7)
                for x in range(7)
                if MAZE[y][x] == "."
                and (x, y) not in rooms
                and (x, y) != EXIT
            ]

            point = random.choice(free_cells)
            player.x = point[0]
            player.y = point[1]

            print("Вы переместились в точку:", point)
            room.type = "пустая"

    else:
        print("В комнате ничего нет.")


print('Добро пожаловать в игру "Лабиринт"!')

player = Player()
rooms = create_rooms()

print("Ваша задача — добраться до выхода.")
print("P - игрок, E - выход, # - стена")
print("I - предметы, M - монстр, T - ловушка, O - портал")

while True:
    print("\nЗдоровье:", player.health)
    print("Координаты:", player.x, player.y)

    command = input(
        "Введите направление, 'карта', 'инвентарь' или 'выход': "
    ).lower().strip()

    if command == "выход":
        print("Вы покинули игру.")
        break

    elif command == "карта":
        show_map(player, rooms)
        continue

    elif command == "инвентарь":
        inventory_management(player)
        continue

    if not player.move(command):
        continue

    point = (player.x, player.y)

    if point == EXIT:
        print("Поздравляем! Вы нашли выход!")
        break

    room = rooms.get(point)

    if room is not None:
        interaction(player, room, rooms)

    if player.health <= 0:
        print("Вы погибли. Игра окончена.")
        break
