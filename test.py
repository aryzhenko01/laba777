def check_int():
    while True:
        try:
            i = int(input('Введите элемент: '))
            return i
        except ValueError:
            print('Вы ввели не число')

def check_str():
    while True:
        i = input('Введите ключ: ')
        if i.isdigit():
            print('это число, а не строка')
            continue
        return i

def add_dict(d):
        key=check_str()
        elem = check_int()
        if key not in d:
            d[key]=[elem]
        else:
            d[key].append(elem)
        return d

def find_elem(d):
    while True:
        key = check_str()
        if key in d:
            x=d[key]
            return x
        else:
            print('Такого ключа нет в словаре')

def del_elem(d):
    while True:
        key = check_str()
        if key in d:
            del d[key]
            return d
        else:
            print('Такого ключа нет в словаре')

def print_dict(d):
    for key in d:
        print(f"Ключ: {key} \nЭлементы: {d[key]}\n")

d={'lada': ["Priora", 'Granta','Vesta','Iskra'],
   'bmw': ['M5','M4','M3','M2'],
   'vaz': [2106,2107,2199,2114]}


while True:
    print("\n" + "=" * 40)
    print("МЕНЮ")
    print("=" * 40)
    print("1. Вывести словарь")
    print("2. Добавить элемент в словарь")
    print("3. Найти элемент по ключу")
    print("4. Удалить элемент по ключу")
    print("5. Вывести список ключей")
    print("6. Выход")
    print("=" * 40)

    try:
        choice = int(input("Выберите действие (1-6): "))
    except ValueError:
        print("Ошибка: введите число от 1 до 6")
        continue

    if choice == 1:
        print("\nТекущий словарь:")
        print_dict(d)

    elif choice == 2:
        print("\nДобавление элемента:")
        d = add_dict(d)
        print("Элемент добавлен")

    elif choice == 3:
        print("\nПоиск элемента:")
        result = find_elem(d)
        if result is not None:
            print(f"Найденный элемент: {result}")

    elif choice == 4:
        print("\nУдаление элемента:")
        d = del_elem(d)
        print("Элемент удален")

    elif choice == 5:
        print("\nСписок ключей:")
        print(list(d.keys()))

    elif choice == 6:
        print("Выход из программы")
        break

    else:
        print("Неверный выбор. Введите число от 1 до 6")