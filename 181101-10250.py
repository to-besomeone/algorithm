T = int(input())

for _ in range(T):
    H, W, N = list(map(int, input().split()))
    j = 1
    while N > H:
        N -= H
        j += 1

    print('%d%02d' % (N,j))