'''
Условие
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите значение наибольшего элемента последовательности.
'''
#**************************************************
a=[]
while True:
    d=int(input())
    if d==0:
        break
    a.append(d)
print(max(a))