'''
Условие
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните 
его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
''' 
n,m = [int(i) for i in input().split()]
a=[['*']*m for i in range(n)]
for i in range(0,n,2):
    for j in range(0,m,2):
        a[i][j]='.'
for i in range(1,n,2):
    for j in range(1,m,2):
        a[i][j]='.'
for row in a:
    print(' '.join(row))



'''
Решение разработчиков
n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))

'''