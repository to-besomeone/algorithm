arr = []
for i in range(9):
    arr.append(int(input()))

maxValue = arr[0]
j = 0
for i in range(1, 9):
    if arr[i] > maxValue :
        maxValue = arr[i]
        j = i
print(maxValue)
print(j+1)