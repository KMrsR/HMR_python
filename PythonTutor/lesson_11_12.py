'''
Условие
В генеалогическом древе определите для двух элементов их наименьшего общего 
предка (Lowest Common Ancestor). Наименьшим общим предком элементов A и B 
является такой элемент C, что С является предком A, C является предком B, 
при этом глубина C является наибольшей из возможных. При этом элемент 
считается своим собственным предком.

Формат входных данных аналогичен предыдущей задаче

Для каждого запроса выведите наименьшего общего предка данных элементов.
''' 
def look(man,x):
    if man not in cp:
        return x
    else:
        x.add(cp[man])
        return look(cp[man],x)
     
cp = dict()
for i in range(int(input())-1):
    c,p = input().split()
    cp[c] = p

for i in range(int(input())):
    m1,m2 = input().split()
    y = set() 
    z = set() 
    if m1 == m2:
        print(m1)
    elif m1 in look(m2,z):
        print(m1)
    elif m2 in look(m1,y):
        print(m2)
    else:
        print(list(look(m1,y).intersection(look(m2,z)))[0])
  


 
'''
def ancestors(child, p_tree):
    result = []
    result.append(child)
    while child in p_tree:
        child = p_tree[child]
        result.append(child)
    return result

p_tree = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent
    
m = int(input())
for i in range(m):
    child_1, child_2 = input().split()
    ancestors_for_1 = set(ancestors(child_1, p_tree))
    for ancestor in ancestors(child_2, p_tree):
        if ancestor in ancestors_for_1:
            print(ancestor)
            break


'''