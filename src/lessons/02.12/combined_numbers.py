# от 1 до 1000, у которых сумма цифр равна числу
for i in range(1, 15):
    dels = 0
    lst = []
    for j in range(1, i+1):
        ost = i % j
        if ost == 0:
            dels = dels + 1
            lst.append(j)
    if not dels == 2:
        print('Число',i,'делится на', lst)
