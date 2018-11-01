N = int(input())
cnt = 0

while N > 1:
    cnt+=1
    N -= 6*cnt
cnt+=1

print(cnt)