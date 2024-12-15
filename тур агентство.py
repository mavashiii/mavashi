import json

# Данные для авторизации
users = {
    "admin": "1234",
    "user": "1234"
}

# Список туров
tours = []


# Функция для авторизации
def authenticate(username, password):
    return users.get(username) == password


# Функция для добавления тура (доступна только администратору)
def add_tour(destination, price):
    tours.append({"destination": destination.strip(), "price": price})


# Функция для удаления тура (доступна только администратору)
def remove_tour(destination):
    global tours
    tours = list(filter(lambda tour: tour["destination"].lower() != destination.lower(), tours))


# Функция для просмотра туров
def view_tours():
    if not tours:
        print("Нет доступных туров.")
        return
    print("\nТуры:")
    print(f"{'Направление':<30} {'Цена':<10}")
    print("-" * 40)
    for tour in tours:
        print(f"{tour['destination']:<30} {tour['price']:<10}")


# Функция для бронирования тура
def book_tour(destination):
    global tours
    for tour in tours:
        if tour["destination"].lower() == destination.lower():
            tours.remove(tour)
            print(f"Вы забронировали тур в '{tour['destination']}' за {tour['price']}!")
            return
    print("Тур не найден.")


# Функция для сортировки туров
def sort_tours():
    global tours
    tours.sort(key=lambda x: x['destination'])


# Функция для фильтрации туров по цене
def filter_tours(min_price, max_price):
    return list(filter(lambda x: min_price <= x['price'] <= max_price, tours))


# Основная логика приложения
def main():
    print("Добро пожаловать в туристическое агентство!")

    # Авторизация
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    if not authenticate(username, password):
        print("Неверное имя пользователя или пароль.")
        return

    is_admin = username == "admin"

    while True:
        print("\nВыберите действие:")
        if is_admin:
            print("1. Добавить тур")
            print("2. Удалить тур")
        print("3. Просмотреть туры")
        print("4. Забронировать тур")
        print("5. Сортировать туры")
        print("6. Фильтровать туры по цене")
        print("7. Выйти")

        choice = input("Ваш выбор: ")

        try:
            if is_admin and choice == '1':
                destination = input("Введите направление тура: ")
                price = float(input("Введите цену тура: "))
                add_tour(destination, price)
                print(f"Тур в '{destination}' добавлен.")
            elif is_admin and choice == '2':
                destination = input("Введите направление тура для удаления: ")
                remove_tour(destination)
                print(f"Тур в '{destination}' удален.")
            elif choice == '3':
                view_tours()
            elif choice == '4':
                destination = input("Введите направление тура для бронирования: ")
                book_tour(destination)
            elif choice == '5':
                sort_tours()
                print("Туры отсортированы по направлению.")
            elif choice == '6':
                min_price = float(input("Введите минимальную цену: "))
                max_price = float(input("Введите максимальную цену: "))
                filtered_tours = filter_tours(min_price, max_price)
                print("\nОтфильтрованные туры:")
                for tour in filtered_tours:
                    print(f"Направление: {tour['destination']}, Цена: {tour['price']}")
            elif choice == '7':
                print("Вы вышли из приложения.")
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, введите корректные данные.")

if __name__ == "__main__":
    main()
