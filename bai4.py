def gt(x):
    tmp = 1
    for i in range(1, x+1):
        tmp *= i
    return tmp
n = int(input())
x = int(input())
tong = 0
for i in range(1, 2*n+2, 2):
    tong += x**i / gt(i)
print(tong)