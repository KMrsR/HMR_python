import matplotlib.pyplot as plt
import random
'''
fig = plt.figure()# Добавление на рисунок прямоугольной (по умолчанию) области рисования

scatter1 = plt.scatter(10.0, 20.0)
grid1 = plt.grid(True)   # линии вспомогательной сетки
plt.show()
'''

fig = plt.figure()# Добавление на рисунок прямоугольной (по умолчанию) области рисования
x1=0
y1=0
x2=250
y2=500
x3=500
y3=0
x_f=random.randint(0,500)
y_f=random.randint(0,500)

scatter1 = plt.scatter(x1,y1)
scatter1 = plt.scatter(x2,y2)
scatter1 = plt.scatter(x3,y3)
scatter1 = plt.scatter(x_f, y_f)
x_cur=x_f
y_cur=y_f

<<<<<<< HEAD
for number in range(0,100):
=======
for number in range(0,5000):
>>>>>>> f8c7696ff862cdab72b07e58aa03b17eafc246db
	rnd_num=random.randint(1,7)
	if rnd_num==1 or rnd_num==2:
		x_new=x_cur/2
		y_new=y_cur/2
		scatter1 = plt.scatter(x_new,y_new,s = 1)
		x_cur=x_new
		y_cur=y_new
	elif rnd_num==3 or rnd_num==4:
		x_new=(x_cur+250)/2
		y_new=(y_cur+500)/2
		scatter1 = plt.scatter(x_new,y_new,s = 1)
		x_cur=x_new
		y_cur=y_new
	elif rnd_num==5 or rnd_num==6:
		x_new=(x_cur+500)/2
		y_new=y_cur/2
		scatter1 = plt.scatter(x_new,y_new,s = 1)
		x_cur=x_new
		y_cur=y_new

grid1 = plt.grid(True)   # линии вспомогательной сетки
plt.show()