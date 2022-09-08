i, iMax, max = 0, 0, -1
x = int(input())
while x > 0:
    if x > max:
        max = x
        iMax = i
    x = int(input())
    i += 1
else:
    print('ind of max: ', iMax)
