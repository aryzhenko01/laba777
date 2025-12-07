import random
    
def IsPower(K):
    if K>0:
        while K % 5==0:
            K= K//5
        if K==1:
            return True
    return False


l=[]
for i in range(10):
    l.append(random.randint(0,100))
print('Множество чисел:', l)


ch=[]
count=0
for i in l:
    if IsPower(i)==True:
        count+=1
        ch.append(i)


print('Количество чисел, являющихся степенью числа 5:', count, 'Эти числа:', ch )

    
        