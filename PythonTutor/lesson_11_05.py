'''
Условие
В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами 
доступа к файлам. Для каждого файла известно, с какими действиями можно к нему обращаться:
запись W,
чтение R,
запуск X.
В первой строке содержится число N — количество файлов содержащихся в данной файловой системе. 
В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные 
пробелами. Далее указано чиcло M — количество запросов к файлам. В последних M строках указан 
запрос вида Операция Файл. К одному и тому же файлу может быть применено любое колличество 
запросов.

Вам требуется восстановить контроль над правами доступа к файлам (ваша программа для каждого 
запроса должна будет возвращать OK если над файлом выполняется допустимая операция, или же 
Access denied, если операция недопустима.
''' 
n=int(input())
a={}
f = [[] for i in range(n)]

for i in range(n):
    f[i] = input().split()

for i in range(n):
    if 'W' in f[i][1:]:
        if 'write' not in a.keys():
            a['write']=[]
            a['write'].append(f[i][0])
        else:
            a['write'].append(f[i][0])
    if 'R' in f[i][1:]:
        if 'read' not in a.keys():
            a['read']=[]
            a['read'].append(f[i][0])
        else:
            a['read'].append(f[i][0]) 
    if 'X' in f[i][1:]:
        if 'execute' not in a.keys():
            a['execute']=[]
            a['execute'].append(f[i][0])
        else:
            a['execute'].append(f[i][0]) 

m=int(input())
z = [[] for i in range(m)]
for i in range(m):
    z[i] = input().split()


for i in range(m):
    if z[i][0]=='read':
        if z[i][0] in a.keys():
            if z[i][1] in a['read']:
                print('OK')
            else:
                print('Access denied')
        else:
            print('Access denied')
        
        
    if z[i][0]=='write':
        if z[i][0] in a.keys():
            if z[i][1] in a['write']:
                print('OK')
            else:
                print('Access denied')
        else:
            print('Access denied')
    if z[i][0]=='execute':
        if z[i][0] in a.keys():
            if z[i][1] in a['execute']:
                print('OK')
            else:
                print('Access denied')
        else:
            print('Access denied')


'''
ACTION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    action, file = input().split()
    if ACTION_PERMISSION[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')


'''