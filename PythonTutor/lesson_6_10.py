'''
Условие
Определите количество четных элементов в последовательности, 
завершающейся числом 0.
'''
a=[]
c=0
while True:
    d=int(input())
    if d==0:
        break
    a.append(d)
for i in range(len(a)):
    if a[i]%2==0:
        c+=1
print(c)