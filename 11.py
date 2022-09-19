# Задание 7. Страны и города. Дан список стран и городов каждой страны.
# Затем даны названия городов. Для каждого города укажите, в какой стране он
# находится.

# Входные данные
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# 3
# Odessa
# Moscow
# Novgorod
# Правильный ответ
# Ukraine
# Russia
# Russia

countries_and_towns = {}

for i in range(int(input())):
    country, *towns = input().split()
    for town in towns:
        countries_and_towns[town] = country

print(countries_and_towns)

for i in range(int(input())):
    print(countries_and_towns[input()])
