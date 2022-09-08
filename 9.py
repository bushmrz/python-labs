# Даны два числа n и m . Создайте
# двумерный массив размером n×m и заполните его символами «.» и «*» в
# шахматном порядке. В левом верхнем углу должна стоять точка.

a = '.'
b = '*'
n = int(input())
m = int(input())

x = [[a]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i+j)%2 == 1:
            x[i][j] = b

for row in x:
    print(' '.join(row))






