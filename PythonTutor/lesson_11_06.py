'''
Условие
Дан список стран и городов каждой страны. Затем даны названия городов. Для 
каждого города укажите, в какой стране он находится.
''' 
countries = {}
for i in range(int(input())):
    country, *city = input().split()
    countries[country] = city

for i in range(int(input())):
    f=input()
    for city in countries.keys():
        if f in countries[city]:
            print(city) 

'''
motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country
        
for i in range(int(input())):
    print(motherland[input()])
'''