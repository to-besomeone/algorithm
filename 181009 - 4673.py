def d(n):
    result = n
    while n != 0:
        result += n % 10

        n = n // 10
    return result


arr = [0] * 20000

for i in range(1, 10001):
    arr[d(i)] = i
    if arr[i] == 0:
        print(i)