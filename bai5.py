def gt(x):
    tmp = 1
    for i in range(1, x+1):
        tmp *= i
    return tmp
a = float(input())
tong = 0
i = 1
while True:
    tong += 1/gt(i)
    if 1/(i) < a:
        print(round(tong, 2))
        break
    i += 2