l = list(map(int, input().split()))
for i in l:
    if i != l[0]:
        print("False")
        break
else:
    print("True")