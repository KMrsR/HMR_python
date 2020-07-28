'''
Условие
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. 
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
''' 
x=[0]*8
y=[0]*8
m=[]
for i in range(8):
    x[i],y[i]= [int(s) for s in input().split()]
for i in range(7):
    for j in range(i+1,7):
        if x[i]==x[j]:
            m.append(1)
        elif y[i]==y[j]:
            m.append(1)
        elif abs(x[i]-x[j])==abs(y[i]-y[j]):
            m.append(1)
        else:
            m.append(0)
if m.count(1)>0:
    print("YES")
else:
    print("NO")

