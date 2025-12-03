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

f = check('Введите количество строк списка: ')
t = check('Введите количество элементов строки: ')
print(f"Размер матрицы: {f}x{t}")


matr=[]
for i in range(f):
    elem=[]
    for j in range(t):
        elem.append(random.randint(-100,100))
    matr.append(elem)
print('Полученный список ',matr)

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
print('Матрица по убыванию характеристик', matr)
print('Характеристики строк: ', sum)


