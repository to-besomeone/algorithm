
arr = [0] * 26
maxV = 0
maxVI = 0
str = input()

for i in range(len(str)):
    if ord(str[i]) > 96 :
        arr[ord(str[i])-97] += 1
    else:
        arr[ord(str[i])-65] += 1

for i in range(26):
    if arr[i] > maxV:
        maxV = arr[i]
        maxVI = i
    elif maxV != 0:
        if arr[i]==maxV:
            maxVI = -2

print(chr(maxVI+65))

