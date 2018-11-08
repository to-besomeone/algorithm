k = input()
w = input()
cnt = 0
for i in range(len(w)-1):
    p1 = k.find(w[i])
    p2 = k.find(w[i+1])
    cnt += abs(p2-p1)

print(cnt)