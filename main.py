import random
def check(i):
    while True:
        try:
            b = int(input(i))
            if b > 0:
                return b
            else:
                print('Введенное число некорректно. Число должно быть больше 0.')
        except ValueError:
            print('Вы ввели не число')


def print_matr(x):
    for row in x:
        for elem in row:
            print(f" {elem:5}", end=' ')
        print()


f = check('Введите размерность матрицы: ')
print(f"Размер матрицы: {f}x{f}")


matr=[]
for i in range(f):
    elem=[]
    for j in range(f):
        elem.append(random.randint(-100,100))
    matr.append(elem)
print('Полученная матрица:')
print_matr(matr)

sum=[]
for i in range(len(matr)):
    total=0
    for j in range(len(matr[i])):
        if matr[i][j]%2==0 and matr[i][j]>0:
            total+=matr[i][j]
    sum.append(total)

v=[]
for i in range(len(sum)):
    for j in range(i+1,len(sum)):
        if sum[i] < sum[j]:
            sum[i], sum[j] = sum[j], sum[i]
            matr[i], matr[j] =  matr[j], matr[i]

print('Матрица по убыванию характеристик')
print_matr(matr)

print('Характеристики строк: ', sum)


