'''
Условие
Дан список из чисел и индекс элемента в списке k. Удалите из списка 
лемент с индексом k, сдвинув влево все элементы, стоящие правее 
элемента с индексом k.
Программа получает на вход список, затем число k. Программа сдвигает 
все элементы, а после этого удаляет последний элемент списка при 
помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а 
не делать это при выводе элементов. Также нельзя использовать 
дополнительный список. Также не следует использовать метод pop(k) 
с параметром.
'''  
a = input().split()
k=int(input())

for i in range(len(a)):
    a[i] = int(a[i])
a=a[:k]+a[k+1:]

for i in range(len(a)):
    print(a[i],end=' ')