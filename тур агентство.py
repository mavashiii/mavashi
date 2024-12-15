import json

# Данные для авторизации
users = {
    "admin": "1234",
    "user": "1234"
}

# Список товаров
products = []


# Функция для авторизации
def authenticate(username, password):
    return users.get(username) == password


# Функция для добавления товара (доступна только администратору)
def add_product(name, price):
    products.append({"name": name.strip(), "price": price})


# Функция для удаления товара (доступна только администратору)
def remove_product(name):
    global products
    products = list(filter(lambda product: product["name"].lower() != name.lower(), products))


# Функция для просмотра товаров
def view_products():
    if not products:
        print("Нет доступных товаров.")
        return
    print("\nТовары:")
    print(f"{'Название':<20} {'Цена':<10}")
    print("-" * 30)
    for product in products:
        print(f"{product['name']:<20} {product['price']:<10}")


# Функция для покупки товара
def buy_product(name):
    global products
    for product in products:
        if product["name"].lower() == name.lower():
            products.remove(product)
            print(f"Вы купили товар '{product['name']}' за {product['price']}!")
            return
    print("Товар не найден.")


# Функция для сортировки товаров
def sort_products():
    global products
    products.sort(key=lambda x: x['name'])


# Функция для фильтрации товаров по цене
def filter_products(min_price, max_price):
    return list(filter(lambda x: min_price <= x['price'] <= max_price, products))


# Основная логика приложения
def main():
    print("Добро пожаловать в продуктовый магазин!")

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
            print("1. Добавить товар")
            print("2. Удалить товар")
        print("3. Просмотреть товары")
        print("4. Купить товар")
        print("5. Сортировать товары")
        print("6. Фильтровать товары по цене")
        print("7. Выйти")

        choice = input("Ваш выбор: ")

        try:
            if is_admin and choice == '1':
                name = input("Введите название товара: ")
                price = float(input("Введите цену товара: "))
                add_product(name, price)
                print(f"Товар '{name}' добавлен.")
            elif is_admin and choice == '2':
                name = input("Введите название товара для удаления: ")
                remove_product(name)
                print(f"Товар '{name}' удален.")
            elif choice == '3':
                view_products()
            elif choice == '4':
                name = input("Введите название товара для покупки: ")
                buy_product(name)
            elif choice == '5':
                sort_products()
                print("Товары отсортированы по названию.")
            elif choice == '6':
                min_price = float(input("Введите минимальную цену: "))
                max_price = float(input("Введите максимальную цену: "))
                filtered_products = filter_products(min_price, max_price)
                print("\nОтфильтрованные товары:")
                for product in filtered_products:
                    print(f"Название: {product['name']}, Цена: {product['price']}")
            elif choice == '7':
                print("Вы вышли из приложения.")
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, введите корректные данные.")

if __name__ == "__main__":
    main()
