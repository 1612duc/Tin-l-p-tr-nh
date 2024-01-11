def ams(x):
    tong = 0
    a = x
    while a > 0:
        tong += (a % 10)**len(str(x))
        a //= 10
    if tong == x:
        return True
    return False
n = int(input())
for i in range(n):
    if ams(i):
        print(i)