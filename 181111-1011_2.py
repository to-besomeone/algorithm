T = int(input())

for _ in range(T):
    x, y = list(map(int, input().split(' ')))
    distance = y-x
    ans = 0
    for i in range(1, pow(2,31)):
        if distance >= pow(i,2) and distance < pow(i+1,2):
            distance = distance - pow(i,2)
            tmp1 = distance // i
            tmp2 = distance / i
            if tmp1 == tmp2:
                print(i*2-1+tmp1)
                break
            else:
                print(i*2-1+tmp1+1)
                break