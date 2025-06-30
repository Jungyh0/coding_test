a = []
b = []
t = False
for i in range(28):
    a.append(int(input()))

for i in range(1, 31):
    b.append(i)

for i in range(len(b)):
    t = False
    for j in range(len(a)):
        if b[i] == a[j]:
            t = True
    if t == False:
        print(b[i])
        
