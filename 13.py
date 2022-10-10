# Задание 1 Создайте класс Cat. Определите атрибуты name (имя), color
# (цвет) и weight (вес). Добавьте метод под названием meow («мяуканье»).
# Создайте объект класса Сat, установите атрибуты, вызовите метод meow.
# Задание 2

# 1 Напишите код, описывающий класс Animal:
# • добавьте атрибут имени животного;
# • добавьте метод eat(), выводящий «Намнём»;
# • добавьте методы getName() и setName();
# • добавьте метод makeNoise(), выводящий «Имя животного говорит Гррр»;
# • добавьте конструктор классу Animal, выводящий «Родилось животное имя животного».

# 2 Основная программа:
# • создайте животное, в момент создания определите его имя;
# • узнайте имя животного через вызов метода getName();
# • измените имя животного через вызов метода setName();
# • вызовите eat() и makeNoise() для животного.
import math

# class Animal():
#     name = ''
#
#     def __init__(self, newName):
#         self.name = newName
#         print('Родилось животное ', self.name)
#
#     def setName(self, newName):
#         self.name = newName
#
#     def getName(self):
#         return (self.name)
#
#
#     def eat(self):
#         print(self.name, 'кушает')
#
#     def makeNoise(self):
#         print(self.name,' говорит:  хочу кушать')
#
# class Cat():
#     name = ''
#     color = ''
#     weigth = ''
#
#     def __init__(self, newName):
#         self.name = newName
#         print('Родилось животное ', self.name)
#
#     def meow(self):
#         print(self.name, 'мявкает')
#
# def setCatandAni():
#     cat_1 = Cat(input('Введите имя животного: '))
#     cat_1.name = input('Имя кота: ')
#     cat_1.color = input('Цвет кота: ')
#     cat_1.weigth = input('Вес кота: ')
#
#     cat_1.meow()
#
#     newAni = Animal(input('Введите имя животного: '))
#     newAni.makeNoise()
#     newAni.eat()
#     newAni.setName(input('Введите новое имя животного: '))
#     print(newAni.getName())
#


# Задание 3 Создайте класс StringVar для работы со строковым типом
# данных, содержащий методы set() и get(). Метод set() служит для изменения
# содержимого строки, get() – для получения содержимого строки. Создайте
# объект типа StringVar и протестируйте его методы.
class StringVar():

    text = 'Test string'

    def set(self, newValue):
        self.text=newValue

    def get(self):
        return (self.text)

def ex3():
    test_str = StringVar()
    print(test_str.get())
    test_str.set(input('Введите новое значение строки:'))
    print(test_str.get())


# Задание 4 Создайте класс точка Point, позволяющий работать с
# координатами ( , ). Добавьте необходимые методы класса.
class Point():
    x, y = 0, 0

    def __init__(self, X, Y):
        self.x=X
        self.y=Y

    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def getPoint(self):
        return (self.x, self.y)

    def getX(self):
        return(self.x)

    def getY(self):
        return(self.y)

    def distance(self, point):
        return math.sqrt(abs(pow(self.x, 2)-pow(point.x, 2) + pow(self.y, 2)-pow(point.y, 2)))

def points():
    first_point = Point(3,4)
    print(first_point.getPoint())
    second_point = Point(1,2)
    print(second_point.getX(), ',', second_point.getY())
    print(first_point.distance(second_point))


# Задание 5 Пусть Animal будет родительским для класса Cat. Метод
# makeNoise() класса Cat выводит «Имя животного говорит Мяу». Конструктор
# класса Cat выводит «Родился кот», а также вызывает родительский
# конструктор.

# Задание 6 Пусть Animal будет родительским для класса Dog. Метод
# makeNoise() для Dog выводит «Имя животного говорит Гав». Конструктор Dog
# выводит «Родилась собака», а также вызывает родительский конструктор.

# Задание 7 Основная программа. Код, создающий кота, двух собак и
# одно простое животное. Дайте имя каждому животному (через вызов методов).
# Код, вызывающий eat() и makeNoise() для каждого животного.


class Animal():
    name = ''

    def __init__(self, newName):
        self.name = newName
        print('Родилось животное ', self.name)

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return (self.name)

    def eat(self):
        print(self.name, 'кушает')

    def makeNoise(self):
        print(self.name, ' говорит:  хочу кушать')


class Cat(Animal):
    name = ''

    def __init__(self, newCat):
        self.name = newCat
        Animal.__init__(self, newCat)
        print('Родился котенок ', self.name)

    def makeNoise(self):
        print(self.name, 'мявкает')


class Dog(Animal):
    name = ''
    color = ''
    weigth = ''

    def __init__(self, newDog):
        self.name = newDog
        Animal.__init__(self, newDog)
        print('Родилась собака ', self.name)

    def makeNoise(self):
        print(self.name, 'гавкает')


def newAnimals():
    kitten = Cat('Мурзик')
    kitten2 = Cat('Новый Мурзик')
    dog = Dog('Собака')
    rat = Animal('Коврик')

    print('\n')

    kitten.makeNoise()
    kitten2.makeNoise()
    dog.makeNoise()
    rat.makeNoise()

    print('\n')

    kitten.eat()
    kitten2.eat()
    dog.eat()
    rat.eat()

newAnimals()
# setCatandAni()
# ex3()
# points()


