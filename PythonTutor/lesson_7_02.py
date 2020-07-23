
'''
Условие
Выведите все четные элементы списка. При этом используйте цикл for, 
перебирающий элементы списка, а не их индексы!
'''
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(a)):
    if a[i]%2==0:
        print(a[i],end=' ')
