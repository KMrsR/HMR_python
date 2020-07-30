'''
Условие
Даны два списка чисел. Найдите все числа, которые входят как в первый, 
так и во второй список и выведите их в порядке возрастания.
Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
''' 
a=sorted(set([int(i) for i in input().split()]) & set([int(i) for i in input().split()]))
for i in range(len(a)):
    print(a[i],end=' ')

'''
Решение разработчиков
print(*sorted(set(input().split()) & set(input().split()), key=int))
'''


