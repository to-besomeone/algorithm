
for i in range(int(input())):
    stack = []
    parth = input()
    for j in range(len(parth)):
        if parth[j] == '(':
            stack.append(parth[j])
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(parth[j])

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")