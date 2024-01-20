l = input().split()
n = 10**9
m = ""
for i in l:
    if i.isnumeric() and int(i) < n:
        n = int(i)
    elif len(i) > len(m):
        m = i
print(m, n)