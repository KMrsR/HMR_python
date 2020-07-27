'''
Условие
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). 
Если элементов нечетное число, то последний элемент остается на своем месте.

Решение разработчиков
a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))
'''  
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
    
if len(a)%2==0:
    b=[0]*len(a)
    for i in range(0,len(a),2):
        b[i]=a[i+1]
        b[i+1]=a[i]
else:
    b=[0]*(len(a)-1)
    for i in range(0,len(a)-1,2):
        b[i]=a[i+1]
        b[i+1]=a[i]
    b.append(a[len(a)-1])

for i in range(len(b)):
    print(b[i],end=' ')
