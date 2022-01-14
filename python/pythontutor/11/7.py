# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

dic = {}

for i in range(int(input())):
    country, *towns = [name for name in input().split()]
    for town in towns:
        dic[town] = country

for j in range(int(input())):
    print(dic[input()])
