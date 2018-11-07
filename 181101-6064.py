T = int(input())

for _ in range(T):
    M, N, x, y = list(map(int, input().split(' ')))
    i ,j, cnt = 1, 1, 1
    while True:
        if i == x and j == y:
            break
        if i < M:
            i += 1
        else:
            i = 1
        if j < N:
            j += 1
        else:
            j = 1
        if i == M and j == N:
            break
        cnt += 1
    if i == M and j == N:
        print(-1)
    else:
        print(cnt)