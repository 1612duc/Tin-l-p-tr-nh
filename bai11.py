def tlp(x):
    if x == 0:
        return ""
    so = "0123456789ABCDEF"
    return so[x%16] + tlp(x//16)
n = int(input())
print(tlp(n))