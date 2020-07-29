'''
Условие
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с 
номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем элементы массива, 
затем числа i и j.
Решение оформите в виде функции swap_columns(a, i, j).
'''

def swap_columns(a, i, j):
    b=[]
    c=[]
    for row_ind in range(n):
        for elem_ind in range(m):
            if elem_ind==i :
                b.append(a[row_ind][j])
            elif elem_ind==j :
                b.append(a[row_ind][i])
            else:
                b.append(a[row_ind][elem_ind])
    for i in range(0,len(b),6):
        c.append(b[i:i+6])
    return c

a = []
n,m=[int(i) for i in input().split()]
for i in range(n):
    a.append([int(j) for j in input().split()])
i,j=[int(i) for i in input().split()] 

for row in swap_columns(a, i, j):
    print(' '.join([str(elem) for elem in row]))




'''
Решение разработчиков
def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))




'''