def np(x):
    kq = ""
    while x > 0:
        du = x % 2
        kq = str(du) + kq
        x //= 2
    return kq

n = list(map(int, input().split(",")))
for i in n:
    print(np(i))
