'''
Условие
Определите сумму всех элементов последовательности, 
завершающейся числом 0. В этой и во всех следующих задачах 
числа, следующие за первым нулем, учитывать не нужно.

'''
#**************************************************
d=0
while True:
    a=int(input())
    if a==0:
        break
    d+=a
print(d)

