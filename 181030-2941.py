str = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

string = input()

for i in str:
    string = string.replace(i, "*")

print(len(string))