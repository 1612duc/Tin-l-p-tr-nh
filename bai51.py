a = input()
n = ""
dem = 0
for i in range(-1, -len(a) - 1, -1):
    dem += 1
    n = a[i] + n
    if dem % 3 == 0:
        n = "." + n
    print(n)
print(n)