'''
Условие
Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. 
Беатриса пытается угадать это число, для этого она называет некоторые множества 
натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел есть 
задуманное или NO в противном случае. После нескольких заданныъх вопросов Беатриса 
запуталась в том, какие вопросы она задавала и какие ответы получила и просит вас 
помочь ей определить, какие числа мог задумать Август.

В первой строке задано n - максимальное число, которое мог загадать Август. Далее 
каждая строка содержит вопрос Беатрисы (множество чисел, разделенных пробелом) и 
ответ Августа на этот вопрос.

Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.
''' 
n=int(input())
st=set()

for i in range(1,n+1):
    st.add(i)
    
a=[]
while True:
    b=input()
    if b=="HELP":
        break
    a.append(b)
    
for j in range(0,len(a),2):   
    a[j]=set([int(i) for i in a[j].split()])

for i in range(1,len(a),2):
    if a[i]=="NO":
        st-=a[i-1]
    elif a[i]=="YES":
        st=st & a[i-1]
    
for num in st:
    print(num, end=' ')


'''
Случайное решение
n, a, ans = int(input()), set(input().split()), ''
b = a
while(b!={'HELP'}):
    ans = input()
    if ans=='NO':
        a-=b
    else:
        a&=b
    b = set(input().split())
print(' '.join(str(s) for s in a))

Решение разработчиков
n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess

print(' '.join([str(x) for x in sorted(possible_nums)]))

'''


