
'''
Условие
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите, сколько элементов этой последовательности больше предыдущего элемента.
'''
a=[]
c=0
while True:
    d=int(input())
    if d==0:
        break
    a.append(d)
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        c+=1
print(c)