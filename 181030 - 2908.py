A ,B= input().split()
C = 0
D = 0
for i in range(3):
    C += int(A[i])*10**i
    D += int(B[i])*10**i

print(max(C, D))

