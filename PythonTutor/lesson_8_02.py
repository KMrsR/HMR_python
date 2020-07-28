'''
Условие
Дано действительное положительное число a и целоe число n.
Вычислите an. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя.
''' 
def power(a,n):
    res=1.0
    if n>0:
        for i in range(n):
            res*=a
    else:
        for i in range(abs(n)):
            res/=a
    return res

a=float(input())
n=int(input())
print(power(a,n))
