N = input()

mat1 = [0 for _ in range(10)]

for i in range(len(N)):
    mat1[int(N[i])] += 1
    if N[i] == '6':
        if mat1[6] > mat1[9]:
            mat1[9] += 1
            mat1[6] -= 1
    if N[i] == '9':
        if mat1[9] > mat1[6]:
            mat1[6] += 1
            mat1[9] -= 1


print(max(mat1))
