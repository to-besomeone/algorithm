N = int(input())

mat = [int(input()) for _ in range(N)]

for i in range(N-1, -1, -1): # for i in range(N-1):
    for j in range(i):          # for j in range(N-1):
        if mat[j] > mat[j+1]:
            tmp = mat[j]
            mat[j] = mat[j+1]
            mat[j+1] = tmp

for i in range(N):
    print(mat[i])