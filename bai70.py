l = input().split()
k = []
for i in range(1, len(l)):
    if (l[i].isnumeric() and l[i-1].isnumeric()) or (l[i].isalpha() and l[i-1].isalpha()):
        print("False")
        break
else:
    if l[0].isalpha():
        del l[0]
    for i in range(0, len(l), 2):
        print(i)
        k[int(i/2)] = int(l[i]) * int(l[i+2])
    print(k)