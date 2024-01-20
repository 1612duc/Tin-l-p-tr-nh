l = list(map(int, input().split()))
kq = -999999999
for i in l:
    if i < 0 and kq < i:
        kq = i
if kq != -999999999:
    print(kq)
else:
    print(0)