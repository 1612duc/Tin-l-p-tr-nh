l = list(map(int, input().split()))
a = int(input())
b = int(input())
kq = 10**9
for i in l:
    if a <= i <= b and kq > i:
        kq = i
print(kq)