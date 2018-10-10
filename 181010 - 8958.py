num = int(input())

for i in range(num):
    scr = input()
    tmp = 0
    rst = 0
    for j in range(len(scr)):
        if scr[j] == 'O':
            tmp+=1
            rst += tmp
        elif scr[j] == 'X':
            tmp = 0
    print(rst)