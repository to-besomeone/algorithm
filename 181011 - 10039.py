result = 0
for i in range(5):
    scr = int(input())
    if scr < 40 :
        scr = 40
    result += scr

print(result // 5)