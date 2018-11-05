N = int(input())

for i in range(N):
    for j in range(i):
        print(" ", end='')
    for k in range(2*(N-i)-1):
        print("*", end='')
    print("")
for i in range(1,N):
    for j in range(1, N-i):
        print(" ", end='')
    for k in range(2*i+1):
        print("*", end='')
    print("")
