'''
Условие
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. 
Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним.


''' 
n=int(input())
a={}
for i in range(n):
    key,val=[str(i) for i in input().split()]
    a[key]=val
find=str(input()) 

if find in a.keys():
    print(a[find])
elif find in a.values():
    for key,val in a.items():
        if val==find:
            print(key)
#print(find)



'''
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])


'''