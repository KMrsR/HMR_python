'''
Условие
Заданы две клетки шахматной доски. Если они покрашены 
в один цвет, то выведите слово YES, а если в разные 
цвета — то NO. Программа получает на вход четыре числа 
от 1 до 8 каждое, задающие номер столбца и номер 
строки сначала для первой клетки, потом для второй клетки.
'''
#**************************************************
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1%2!=0 and y1%2!=0:
	cell1= True	#black
elif x1%2==0 and y1%2==0:
	cell1=True	#black
else:
	cell1=False	#white

if x2%2!=0 and y2%2!=0:
	cell2= True	#black
elif x2%2==0 and y2%2==0:
	cell2=True	#black
else:
	cell2=False	#white

if cell1==False and cell2==False or cell1==True and cell2==True:
	print("YES")
else:
	print("NO")