left, right = list(map(int, input().split(' ')))
mat = [0 for _ in range(right-left+1)]
string = '36'
cnt = 0
for i in range(left, right+1):
    mat[i-left] = str(i)


for i in mat:
    if string in i:
        cnt += 1

print(cnt)