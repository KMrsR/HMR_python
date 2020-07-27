
'''
Условие
Выведите все четные элементы списка. При этом используйте цикл for, 
перебирающий элементы списка, а не их индексы!
'''
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(a)):
    if a[i]%2==0:
        print(a[i],end=' ')



 
'''
Условие
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные:
1 2 3 2 3
Правильный ответ

''' 
'''
Условие
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
Входные данные:
6 9 6 23 12 19 14 26
Правильный ответ
9 23 12 19 14 26
''' 
'''
Условие
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
Входные данные:
20 3
3 8
13 17
6 9
Правильный ответ
II.......III.....III

''' 
'''
Условие
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
Входные данные:
1 8
2 7
3 6
4 5
5 4
6 3
7 2
8 1
Правильный ответ
YES

''' 