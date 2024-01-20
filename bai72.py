l = input().split()
n = 0
m = ""
for i in l:
    dem = 0
    for j in i:
        if j == j.upper():
            dem += 1
    if n < dem:
        m = i
print(m, l.index(m))