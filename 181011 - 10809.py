str = input()
num = [-1] * 26

for i in range(len(str)):
    if num[ord(str[i])-97]!=-1:
        continue
    num[ord(str[i])-97] = i

for i in range(26):
    print(num[i], end=' ')