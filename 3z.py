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

#main
print('Исходный словарь: ')
print_dict(d)
print(f"Добавить элементы в словарь: ")
add_dict(d)
print(f'Полученный словарь: ')
print_dict(d)
print('Найти элемент по ключу: ')
print(f'Найденный элемент по ключу: {find_elem(d)}')
print('Удалить элемент по ключу')
print_dict(del_elem(d))
print('Ключи словаря:')
print(d.keys())

#print(find_elem(d))



