p2 = ["A", "B", "C"] #2 -> 3초
p3 = ["D", "E", "F"] #3 -> 4초
p4 = ["G", "H", "I"] #4 -> 5초
p5 = ["J", "K", "L"] #5 -> 6초
p6 = ["M", "N", "O"] #6 -> 7초
p7 = ["P", "Q", "R", "S"] #7 -> 8초
p8 = ["T", "U", "V"] #8 -> 9초
p9 = ["W", "X", "Y", "Z"] #9 -> 10초

dial = input()
cnt = 0
for i in range(len(dial)):
    if dial[i] in p2:
      cnt += 3
    elif dial[i] in p3:
        cnt+= 4
    elif dial[i] in p4:
        cnt += 5
    elif dial[i] in p5:
        cnt += 6
    elif dial[i] in p6:
        cnt += 7
    elif dial[i] in p7:
        cnt += 8
    elif dial[i] in p8:
        cnt += 9
    else:
        cnt += 10

print(cnt)
