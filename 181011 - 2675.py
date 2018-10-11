N = int(input())

for i in range(N):
    R = list(input().split())
    numb = int(R[0])
    for j in range(len(R[1])):
        for k in range(numb):
            print(R[1][j], end='')
    print()