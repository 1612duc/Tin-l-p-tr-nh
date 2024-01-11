dem = 0 
def move(n, A, B, C,):
    global dem
    if n == 1:
        dem += 1
        print(f"{dem}: Di chuyen dia 1 tu {A} sang {C}")
        return
    else:
        move(n-1, A, C, B)
        dem += 1
        print(f"{dem}: Di chuyen dia {n} tu {A} sang {C}")
        move(n-1, B, A, C)
        
n = int(input())
move(n, "A", "B", "C")