'''
Условие
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию 
с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Поскольку при этом количество элементов в списке увеличивается, после считывания списка 
в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при 
выводе и не создавая дополнительного списка.

Входные данные:
7 6 5 4 3 2 1
2 0
Правильный ответ
7 6 0 5 4 3 2 1
''' 
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
b = input().split()
for i in range(len(b)):
    b[i] = int(b[i])
k=b[0]
c=b[1]

a.append(0)
for i in range(len(a)-1,k,-1):
	a[i]=a[i-1]
a[k]=c

for i in range(len(a)):
    print(a[i],end=' ')

