calebe = [['calebe', 19], ['João', 13], ['maria', 12], ['arroz', 41],]

usuario = 'calebe'

i = 0
j = 0

for i in range (len(calebe)):
    for j in range(i):
        if usuario in calebe[i][j]:
            i = i
            j = j
            break
        break

print(calebe[i])
    
