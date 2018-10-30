str = input()
arr=[]


while str!="":
    if str[0] == "c":
        if str[1] == "=":
            arr.append("c=")
            str = str[2:]
        elif str[1] == "-":
            arr.append("c-")
            str = str[2:]
        else:
            arr.append("c")
            str = str[1:]

    elif str[0] == "d":
        if str[1] == "z":
            if str[2] == "=":
                arr.append("dz=")
                str = str[3:]
        elif str[1] == "-":
            arr.append("d-")
            str = str[2:]
        else:
            arr.append("d")
            str = str[1:]

    elif str[0] == "l":
        if str[1] == "j":
            arr.append("lj")
            str = str[2:]
        else:
            arr.append("l")
            str = str[1:]

    elif str[0] == "n":
        if str[1] == "j":
            arr.append("nj")
            str = str[2:]
        else:
            arr.append("n")
            str = str[1:]

    elif str[0] == "s":
        if str[1] == "=":
            arr.append("s=")
            str = str[2:]
        else:
            arr.append("s")
            str = str[1:]

    elif str[0] == "z":
        if str[1] == "=":
            arr.append("d=")
            str = str[2:]
        else:
            arr.append("z")
            str = str[1:]
    else:
        arr.append(str[0])
        str = str[1:]
    # for i in range(len(str)):
    #     if str[i] == "c":
    #         if str[i+1] == "=":
    #             arr.append("c=")
    #         elif str[i+1] == "-":
    #             arr.append("c-")
    #         else:
    #             arr.append("c")
    #
    #     elif str[i] == "d":
    #         if str[i+1] == "z":
    #             if str[i+2] == "=":
    #                 arr.append("dz=")
    #         elif str[i+1] == "-":
    #             arr.append("d-")
    #         else:
    #             arr.append("d")
    #
    #     elif str[i] == "l":
    #         if str[i+1] == "j":
    #             arr.append("lj")
    #         else:
    #             arr.append("l")
    #
    #     elif str[i] == "n":
    #         if str[i+1] == "j":
    #             arr.append("nj")
    #         else :
    #             arr.append("n")
    #
    #
    #     elif str[i] == "s":
    #         if str[i+1] == "=":
    #             arr.append("s=")
    #         else:
    #             arr.append("s")
    #
    #     elif str[i] == "z":
    #         if str[i-1] != "d" and str[i+1] == "=":
    #             arr.append("d=")
    #         else:
    #             arr.append("z")
    #     else:
    #         arr.append(str[i])


print(arr)
print(len(arr))