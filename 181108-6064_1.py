import math
T = int(input())

for _ in range(T):
    M, N, x, y = list(map(int, input().split(' ')))
    ans = x
    ax = x

    ay = x%N
    if ay == 0:
        ay += N

    if M > N:
        ri = M-N
    else:
        ri = M

    width = (M*N) // math.gcd(M, N) // M

    while width >= 0:
        if ax == x and ay == y:
            break
        ay += ri
        if ay > N:
            ay = ay % N
            if ay == 0:
                ay += N
        ans += M

        width -= 1

    if ax == x and ay == y:
        print(ans)
    else:
        print(-1)
