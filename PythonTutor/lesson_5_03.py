'''
Условие
Дана строка. Разрежьте ее на две равные части (если длина строки — четная, 
а если длина строки нечетная, то длина первой части должна быть на один символ больше). 
Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.
При решении этой задачи не стоит пользоваться инструкцией if.
'''
#**************************************************
import math
s = input()
ln=len(s)
st1=s[:math.ceil(ln/2)]
st2=s[math.ceil(ln/2):]
print(st2+st1)


