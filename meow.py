inventory = []
keys_collected = set()
monsters_defeated = set()

# Объекты игры и их описания
rooms = {
    "комната_с_ключами": "Вы в комнате, где лежат ключи. Найдите ключи, чтобы открыть дверь.",
    "комната_с_монстром": "Вы встретили монстра! Найдите предмет, чтобы победить его.",
    "комната_загадок": "Чтобы выбраться из замка, разгадайте загадку: Что всегда идёт, но никогда не уходит?",
}

items = {
    "ключ": "Ключ, который открывает двери.",
    "меч": "Сильное оружие, чтобы победить монстра.",
}

monsters = ["гоблин", "скелет", "вампир"]

# Функция для показа меню действий
def show_menu():
    print("\nДоступные действия:")
    print("1. Взять предмет")
    print("2. Использовать предмет")
    print("3. Посмотреть инвентарь")
    print("4. Перейти в другую комнату")

# Функция для отображения инвентаря
def show_inventory():
    if inventory:
        print("Ваш инвентарь:", inventory)
    else:
        print("Ваш инвентарь пуст.")

# Функция для уровня 1
def level_1():
    print(rooms["комната_с_ключами"])
    action = input("Введите команду (взять ключ, перейти в комнату с монстром): ").strip().lower()

    if action == "взять ключ":
        inventory.append("ключ")
        keys_collected.add("ключ")
        print("Вы взяли ключ!")
    elif action == "перейти в комнату с монстром":
        if "ключ" in inventory:
            print("Вы открыли дверь и вошли в комнату с монстром.")
            return True  # Переход к следующему уровню
        else:
            print("Дверь закрыта! Вам нужен ключ.")
    else:
        print("Неверная команда. Попробуйте снова.")
    return False

# Функция для уровня 2
def level_2():
    print(rooms["комната_с_монстром"])
    monster = random.choice(monsters)
    action = input(f"Вы встретили {monster}. Введите команду (взять меч, использовать меч): ").strip().lower()

    if action == "взять меч":
        inventory.append("меч")
        print("Вы взяли меч!")
    elif action == "использовать меч":
        if "меч" in inventory:
            monsters_defeated.add(monster)
            print(f"Вы победили {monster}!")
            return True  # Переход к следующему уровню
        else:
            print("У вас нет меча!")
    else:
        print("Неверная команда. Попробуйте снова.")
    return False

# Функция для уровня 3
def level_3():
    print(rooms["комната_загадок"])
    answer = input("Введите ваш ответ: ").strip().lower()

    if answer == "время":
        print("Поздравляем! Вы разгадали загадку и выбрались из замка!")
        return True
    else:
        print("Неправильный ответ. Попробуйте снова.")
    return False

def main():
    print("Добро пожаловать в замок приключений!")
    
    if not level_1():
        while not level_1():
            continue

    if not level_2():
        while not level_2():
            continue

    if not level_3():
        while not level_3():
            continue

    print("Спасибо за игру!")

if __name__ == "__main__":
    main()
