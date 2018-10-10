import sys

T = int(input())

for i in range(T):
    fstNum, sndNum = map(int, sys.stdin.readline().split())
    print(fstNum+sndNum)
