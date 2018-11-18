from sys import stdin
num= int(input())
alist=[]
for case in range(num):
    tot=0
    temp=0
    length=int(input())
    nlist=input()
    if(length%2==1):
        newlen=length//2+1
    else:
        newlen=length//2
    for i in range(newlen):
        temp=0
        for j in range(newlen):
            temp+=int(nlist[i+j])
        if(temp>tot):
            tot=temp
    temp=0
    if(length%2==0):
        tempnum=length//2
        for s in range(tempnum,newlen+tempnum):
            temp+=int(nlist[s])
    if(temp>tot):
        tot=temp
    alist.append(tot)
lenlist=len(alist)
for i in range(lenlist):
    print("Case #"+str(i+1)+":",alist[i])