N = int(input())

mat = [int(input()) for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if mat[i] > mat[j] :
            tmp = mat[i]
            mat[i] = mat[j]
            mat[j] = tmp

for i in range(N):
    print(mat[i])