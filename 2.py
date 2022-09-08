print('Введите координаты первой клетки:')
str1 = int(input())
post1 = int(input())
print('Введите координаты второй клетки:')
str2 = int(input())
post2 = int(input())

if abs(str2 - str1) <= 1:
    if abs(post2-post1) <= 1:
        print('YES')
else:
    print('NO')