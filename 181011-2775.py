T = int(input())
apt = [[0 for a in range(14)] for b in range(15)]
apt[0] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for i in range(1, 15):
    for j in range(14):
        apt[i][j] = apt[i][j-1] + apt[i-1][j]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(apt[k][n-1])