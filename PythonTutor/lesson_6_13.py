

'''
Условие
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
'''
a=[]
b=0
while True:
    d=int(input())
    if d==0:
        break
    a.append(d)
for i in range(len(a)):
    if max(a)==a[i]:
        b+=1
print(b)
