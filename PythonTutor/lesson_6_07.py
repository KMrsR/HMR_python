'''
Условие
Определите среднее значение всех элементов последовательности, 
завершающейся числом 0.
'''
#**************************************************
d=0
i=0
while True:
    a=int(input())
    if a==0:
        break
    d+=a
    i+=1
print(d/i)