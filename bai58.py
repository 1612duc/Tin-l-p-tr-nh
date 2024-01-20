l = list(map(int, input().split()))
x = int(input())
d = kq = 0
for i in l:
    if abs(x) + abs(i) > d:
        d = abs(x) + abs(i)
        kq = i
print(kq)