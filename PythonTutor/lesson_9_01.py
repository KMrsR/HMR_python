'''
Условие
Найдите индексы первого вхождения максимального элемента. Выведите два 
числа: номер строки и номер столбца, в которых стоит наибольший элемент в 
двумерном массиве. Если таких элементов несколько, то выводится тот, у 
которого меньше номер строки, а если номера строк равны то тот, у которого 
меньше номер столбца.
Программа получает на вход размеры массива n и m, затем n строк по m чисел 
в каждой.
''' 
n,m = input().split()
n=int(n)
m=int(m)
a = []
b=[]
for i in range(n):
    a.append([int(j) for j in input().split()])
for i in range(n):
    b.append(max(a[i]))
max=max(b)
for i in range(n):
    if a[i].count(max)>0:
        print(i, a[i].index(max))
        break

'''
Решение разработчиков
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
best_i, best_j = 0, 0
curr_max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i, best_j = i, j
print(best_i, best_j)
'''