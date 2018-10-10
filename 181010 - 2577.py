result = 1
num = [0] * 10
for i in range(3):
    a = int(input())
    result *= a

rst = str(result)
leng = len(rst)

for i in range(leng):
    for j in range(10):
        if int(rst[i]) == j:
            num[j] += 1

for i in range(10):
    print(num[i])