'''
Условие
Дана база данных о продажах некоторого интернет-магазина. Каждая строка 
входного файла представляет собой запись вида Покупатель товар количество, 
где Покупатель — имя покупателя (строка без пробелов), товар — название товара 
(строка без пробелов), количество — количество приобретенных единиц товара.

Создайте список всех покупателей, а для каждого покупателя подсчитайте 
количество приобретенных им единиц каждого вида товаров. Список покупателей, 
а также список товаров для каждого покупателя нужно выводить в 
лексикографическом порядке.




''' 
tb = dict()
while True:
    try:
        name, goods, val = input().split()
        val = int(val)
    except:
        break
    if name not in tb.keys():
        tb[name] = {goods : val}
    else:
        if goods in tb[name].keys():
            tb[name][goods] = tb[name][goods] + val
        else:
            tb[name][goods] = val
            
m_list_key = sorted(tb.keys())
for i in range(len(m_list_key)):
     list_key = sorted(tb[m_list_key[i]].keys())
     print(m_list_key[i]+':')
     for j in range(len(list_key)):
         print(list_key[j],tb[m_list_key[i]][list_key[j]])
         
'''
from collections import defaultdict
from sys import stdin

clients = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    client, thing, value = line.split()
    clients[client][thing] += int(value)
        
for client in sorted(clients):
    print(client + ':')
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])



'''