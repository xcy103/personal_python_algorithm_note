op = 0
for i in range(40):
    for j in range(40):
        if sum(list(map(int,str(i))))+sum(list(map(int,str(j))))<=18:
            op+=1
print(op)