'''
Условие
Во входной строке записана последовательность чисел через пробел. 
Для каждого числа выведите слово YES (в отдельной строке), если это 
число ранее встречалось в последовательности или NO, если не встречалось.
''' 
s=[int(i) for i in input().split()]
print("NO")
for i in range(1,len(s)):
    if s[:i].count(s[i])>0:
        print("YES")
    else:
        print("NO")

'''
numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)
'''


