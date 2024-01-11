def gt(x):
    tmp = 1
    for i in range(1, x+1):
        tmp *= i
    return tmp
n = int(input())
tong = 0
for i in range(1, n+1):
    tong += gt(i)
print(tong)