'''
Условие
С начала суток часовая стрелка повернулась на угол 
в α градусов. Определите на какой угол повернулась 
минутная стрелка с начала последнего часа. Входные 
и выходные данные — действительные числа.
'''
#**************************************************
a=float(input())
angle_1=a%30
print(angle_1*12)


