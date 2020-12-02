mas = []
dels = 0
for i in range(1, 100):
    for j in range(1, i+1):
        if i % j == 0:
            dels = dels + 1
    if dels == 2:
        mas.append(i)
    dels = 0
print(mas)