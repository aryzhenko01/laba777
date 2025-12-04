import random

matr = []
for i in range(5):
    elem = []
    for j in range(5):
        elem.append(random.randint(-100, 100))
    matr.append(elem)

def print_matr(x):
    """Красивый вывод матрицы"""
    for row in x:
        for elem in row:
            print(f"{elem:5}", end=' ')  # :5 - ширина 5 символов
        print()  # Важно: переход на новую строку после каждой строки матрицы

print("Сгенерированная матрица 5x5:")
print_matr(matr)