# Задание 7
# Разработать класс «Студенческая группа». Предусмотреть
# возможность работы с переменным числом студентов, поиска записи по
# какому-либо признаку (фамилия, дата рождения, номер телефона и .д.),
# добавление и удаление записей, сортировки по разным полям.
import operator


class Students_group():

    name = ''
    birthday = ''
    phone = ''
    group_name = ''

    def __init__(self):
        self.name = input('Введите фамилию и имя студента: ')
        # self.birthday = input('Введите дату рождения: ')
        # self.phone = input('Введите номер телефона: ')
        # self.group_name = input('Введите группу: ')


    def add_student_info(self):
        # self.name = input('Введите фамилию и имя студента: ')
        self.birthday = input('Введите дату рождения: ')
        self.phone = input('Введите номер телефона: ')
        self.group_name = input('Введите группу: ')

    def show_student(self):
        print(self.name, self.group_name, self.phone, self.birthday)

    def delete_info(self):
        ind2 = int(input("Выберите действие \n1 - полное удаление \n2 - удаление номера \n3 - удаление номера группы \n"))
        if ind2 == 1:
            del(self.name)
            del(self.phone)
            del(self.group_name)
            del(self.birthday)
        elif ind2 == 2:
            del(self.phone)
        elif ind2 == 3:
            self.group_name = ''
        else:
            print('Такого варианта нет. Данные не были изменены.')


    def change_student(self):
        ind = int(input("Выберите действие \n1 - смена имени и фамилии \n2 - смена номера \n3 - смена номера группы \n"))
        if ind == 1:
            self.name = input('Введите новые фамилию и имя студента: ')
        elif ind == 2:
            self.phone = input('Введите новый номер телефона: ')
        elif ind == 3:
            self.group_name = input('Введите новый номер группы: ')
        else:
            print('Такого варианта нет. Данные не были изменены.')

def creator(n):
    students = []
    for i in range(n):
        students.append(Students_group())
    return students

def add_info(objects):
    for obj in objects:
        print('Заполните данные для студента', obj.name)
        obj.add_student_info()
        obj.show_student()
        print()

def sorted_by_group(objects):
    print('Сортировка студентов по группе: ')
    res2 = sorted(objects, key=operator.attrgetter('group_name'))
    for stud in res2:
        print(stud.name, stud.group_name)

def show_all_students(objects):
    print('Список всех студентов: ')
    for obj in objects:
        obj.show_student()
        print()

n = int(input("Количество добавляемых студентов: "))
objects = []
objects = creator(n)
add_info(objects)
# sorted_by_group(objects)



objects[0].change_student()
objects[0].show_student()

objects[0].delete_info()
show_all_students(objects)

