'''
Условие
Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φn = A. Если А не является числом Фибоначчи, выведите число -1.
'''
import math
a=int(input())
b=[0,1,1]
i=0

if math.sqrt(5*a*a-4)%1!=0 and math.sqrt(5*a*a+4)%1!=0:
	f=True
	print(-1)
else:
	f=False

if not f :
	for i in range(3,a+2):
		b.append(b[i-2]+b[i-1])
		if max(b)==a:
			print(i)
			break		
		i+=1