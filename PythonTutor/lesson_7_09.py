'''
Условие
Дан список, упорядоченный по неубыванию элементов в нем. 
Определите, сколько в нем различных элементов.
''' 
a = input().split()
b=[]
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        b.append(a[i])
print(len(b)+1) 
