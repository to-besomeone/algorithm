N = int(input())

for i in range(N):
    for j in range(i+1):
        print("*", end='')
    for k in range(2*N-2*i-2):
        print(" ", end='')
    for m in range(i+1):
        print("*", end='')
    print("")

for i in range(N):
    for j in range(N-i-1):
        print("*", end='')
    for k in range(2*(i+1)):
        print(" ", end='')
    for m in range(N-i-1):
        print("*", end='')
    print("")
