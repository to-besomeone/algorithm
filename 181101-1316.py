
def group(str):
    for j in range(len(str)):
        k = j+1
        a = j
        while k < len(str):
            if str[j] == str[k]:
                if k != a+1:
                    return False
                a = k
            k += 1

    return True


N = int(input())
res = 0
for i in range(N):
    if group(input()):
        res += 1

print(res)