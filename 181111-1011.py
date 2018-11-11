T = int(input())

for _ in range(T):
    x, y = list(map(int, input().split()))
    distance = y-x
    a = 0
    while True:
        maxdis = 0
        a += 1
        if a%2 == 0:
            maxdis = a//2 * (a//2+1)
        elif a%2 == 1:
            maxdis = a//2 * (a//2+1) + a//2 + 1
        if distance <= maxdis:
            print(a)
            break


