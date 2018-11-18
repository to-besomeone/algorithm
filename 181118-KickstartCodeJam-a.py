T = int(input())
summ = [0 for _ in range(T)]

for i in range(T):
    N, P = list(map(int, input().split()))
    lis = [0 for _ in range(P)]
    summ[i] = 2 ** N

    for j in range(P):
        lis[j] = input()

    lis.sort(key=lambda s: len(s))

    for j in range(len(lis) - 1):
        for k in range(j + 1, len(lis)):
            if lis[j] in lis[k]:
                if lis[k].index(lis[j]) == 0:
                    lis[k] = "0"

    for j in range(len(lis)):
        if lis[j] != "0":
            summ[i] -= 2 ** (N - len(lis[j]))

for i in range(T):
    print("Case #" + str(i + 1) + ": " + str(summ[i]))
