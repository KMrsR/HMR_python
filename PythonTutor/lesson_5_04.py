'''
Условие
Дана строка, состоящая ровно из двух слов, разделенных пробелом. 
Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.
При решении этой задачи не стоит пользоваться циклами и инструкцией if.
'''
#**************************************************
import math
s = input()
a=s.find(' ')
print(s[a+1:]+" "+s[:a])

