N = int(input())
cnt = 1
i, j = 1, 1

while cnt < N:
    # print(str(i) + "/" + str(j)+"\tcnt = ", cnt)
    if i == 1 and j == 1:
        cnt += 1
        j += 1
    elif i == 1:
        if j%2 == 0:
            i += 1
            j -= 1
            cnt += 1
        elif j%2 == 1:
            j += 1
            cnt += 1

    elif j == 1:
        if i%2 == 0:
            i += 1
            cnt += 1
        elif i%2 == 1:
            i -= 1
            j += 1
            cnt +=1


    elif j != 1 or i !=1 :
        k = i+j
        if k % 2 == 0:
            i -= 1
            j += 1
            cnt += 1
        elif k % 2 == 1:
            i += 1
            j -= 1
            cnt += 1
print(str(i) + "/" + str(j))