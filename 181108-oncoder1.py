left, right = list(map(int, input().split(' ')))
cnt = 0

for i in range(left, right+1):
    if '36' in str(i):
        cnt += 1

print(cnt)