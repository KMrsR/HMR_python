'''
Условие
Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, 
которое в этом тексте встречается чаще всего. 
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
''' 
n=int(input())
a={}
for i in range(n):
    key=[str(i) for i in input().split()]
    for j in range(len(key)):
        if key[j] not in a.keys():
            a[key[j]]=1
        else:
            a[key[j]]+=1
b=[]
for key in a:
    b.append(key)
b=sorted(b)
f=0
for i in range(len(b)):
    if a[b[i]]>f:
        f=a[b[i]]
        s=b[i]

print(s)






'''
counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
        
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))




'''