
x = [1, 3, 7, 78, 3, 5, 3, 757, 3, 4, 556, 32, 757, 24, 54, 2]
#    0  1  2  3   4  5  6   7
max = fMax = x[0]
for f in range(len(x)):
    if x[f] > max:
        max = x[f]
        fMax = f
else:
    print('max: ', max,  '\nind of max: ',  fMax)
