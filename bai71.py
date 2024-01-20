l = input().split()
n = ""
for i in l:
    if len(i) > len(n):
        n = i
print(l.index(n))