# Задание 3 Имеется набор данных, состоящий из пар положительных
# целых чисел. Необходимо выбрать из каждой пары ровно одно число так,
# чтобы сумма всех выбранных чисел оканчивалась на 4 и при этом была
# минимально возможной. Гарантируется, что искомую сумму получить можно.
# Программа должна напечатать одно число – минимально возможную сумму, соответствующую условиям задачи.

inf_1 = open('3a.txt', 'r')
inf_2 = open('3b.txt', 'r')

def minSum(file_name):
    n = int(file_name.readline())
    ln = 4
    dMin = [100001]*10
    sum = 0
    for i in range(n):
        a, b = map(int, file_name.readline().split())
        sum += min(a, b)
        d = abs(a - b)
        r = d % 10
        dMinNew = dMin[:]
        for k in range(1, 10):
            r0 = (r + k) % 10
            dMinNew[r0] = min(d + dMin[k], dMinNew[r0])
        dMinNew[r] = min(d, dMinNew[r])
        dMin = dMinNew[:]

    if sum % 10 == ln:
        print(sum)
    else:
        print(sum, sum % 10, dMin)
        r0 = ln - sum % 10
        if r0 < 0: r0 += 10
        print(sum + dMin[r0])

    file_name.close()

minSum(inf_1)
minSum(inf_2)


