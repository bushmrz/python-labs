from collections import defaultdict
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

def ex7():
    countries_and_towns = {}

    for i in range(int(input())):
        country, *towns = input().split()
        for town in towns:
            countries_and_towns[town] = country

    print(countries_and_towns)

    for i in range(int(input())):
        print(countries_and_towns[input()])

# Задание 8 Англо-латинский словарь.

# В первой строке содержится единственное целое число – количество английских слов в словаре.
# Далее следует описаний. Каждое описание содержится в отдельной строке, в которой записано сначала английское слово,
# затем отделённый пробелами дефис, затем разделённые запятыми с пробелами переводы этого английского слова на латинский.
# Все слова состоят только из маленьких латинских букв.
# Переводы отсортированы в лексикографическом порядке.
# Порядок следования английских слов в словаре также лексикографический.
# Выведите соответствующий данному латинско-английский словарь, в точности соблюдая формат входных данных.
# В частности, первым должен перевод лексикографически минимального латинского слова, далее – второго в этом порядке и т.д.
# Внутри перевода английские слова должны быть также отсортированы лексикографически.
def ex8():
    latin_to_eng = defaultdict(list)
    for i in range(int(input())):
        eng_word, latin_trans_chunk = input().split(' - ')
        latin_trans = latin_trans_chunk.split(', ')
        for latin_word in latin_trans:
            latin_to_eng[latin_word].append(eng_word)

    print(len(latin_to_eng))
    for latin_word, eng_trans in sorted(latin_to_eng.items()):
        print(latin_word + ' - ' + ', '.join(eng_trans))

# Задание 13 Родословная: LCA. В генеалогическом древе определите для двух элементов их наименьшего общего предка
# (Lowest Common Ancestor). Наименьшим общим предком элементов A и B является такой элемент C,
# что С является предком A, C является предком B, при этом глубина C является наибольшей из возможных.
# При этом элемент считается своим собственным предком.
def ex13():
    def ancestors(child, p_tree):
        result = []
        result.append(child)
        while child in p_tree:
            child = p_tree[child]
            result.append(child)
        return result


    tree = dict()
    n = int(input())
    for i in range(n - 1):
        child, parent = input().split()
        tree[child] = parent

    m = int(input())
    for i in range(m):
        child_1, child_2 = input().split()
        ancestors_for_1 = set(ancestors(child_1, tree))
        for ancestor in ancestors(child_2, tree):
            if ancestor in ancestors_for_1:
                print(ancestor)
                break
# ex7()
# ex8()
# ex13()