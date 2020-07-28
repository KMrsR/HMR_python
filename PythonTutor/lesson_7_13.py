'''
Условие
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую 
необходимо посчитать.

Решение разработчиков
a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)

''' 
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

a = [int(s) for s in input().split()]
a.sort(reverse=False)
b=[]
c=[]
for i in range(len(a)):
    if a[i-1]!=a[i]:
        b.append(a[i])
for i in range(len(b)):
    c.append(a.count(b[i]))
sum=0
for i in range(len(c)):
    if c[i]>1:
        sum+=fac(c[i])/(fac(c[i]-2)*2)
if b==[]:
    sum+=fac(len(a))/(fac(len(a)-2)*2)

print(int(sum))