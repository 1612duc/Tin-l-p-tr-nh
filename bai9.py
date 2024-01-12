def snt(x):
    if x == 2:
        return True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def ucln(x, y):
    ucln = 1
    for i in range(2, min(x, y)+1):
        while x % i == 0 and y % i == 0 and snt(i):
            ucln *= i
            x //= 2
            y //= 2
    return ucln
n = list(map(int, input().split("/")))
if n[1] / ucln(n[0], n[1]) == 1:
    print(int(n[0] / ucln(n[0], n[1])))
else:
    print(str(int(n[0] / ucln(n[0], n[1])))+"/"+str(int(n[1] / ucln(n[0], n[1]))))