
mel = list(map(int, input().split()))

melstr = ""

for i in range(8):
    melstr += str(mel[i])

if melstr == '12345678':
    print("ascending")
elif melstr == '87654321':
    print("descending")
else:
    print("mixed")