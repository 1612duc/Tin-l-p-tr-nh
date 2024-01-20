l = list(map(int,input().split()))
a = []
b = []
c = []
for i in l:
    if i == 0:
        a.append(i)
    elif i % 2 == 0:
        b.append(i)
    else:
        c.append(i)
print(b + a + c)