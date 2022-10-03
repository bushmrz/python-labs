# Задание 3 Имеется набор данных, состоящий из пар положительных
# целых чисел. Необходимо выбрать из каждой пары ровно одно число так,
# чтобы сумма всех выбранных чисел оканчивалась на 4 и при этом была
# минимально возможной. Гарантируется, что искомую сумму получить можно.
# Программа должна напечатать одно число – минимально возможную сумму, соответствующую условиям задачи.

inf_1 = open('3a.txt', 'r')
inf_2 = open('3b.txt', 'r')

def minSum(file_name):
    arr_ost = [10001]*10
    n = int(file_name.readline())
    sum = 0
    for i in range(n):
        text = file_name.readline()
        a, b = text.split()
        a = int(a)
        b = int(b)
        if (arr_ost[abs(a-b)%10] > abs(a-b)):
            arr_ost[abs(a-b)%10] = abs(a-b)
        sum += min(a,b)

    print(sum)

    cheking = False
    if sum%10 != 4:
        for i in range(10):
            if ((sum + arr_ost[i]) % 10 == 4 and arr_ost!= 10001):
                cheking = True
                break



minSum(inf_2)
# 3+1 8+4 0+4 7+7 2+2
