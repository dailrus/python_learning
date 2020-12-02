for i in range(1, 15):
    dels = 0
    lst = []
    for j in range(1, i+1):
        ost = i % j
        if ost == 0:
            dels += dels
            lst.append(j)
    if not dels == 1:
        print('Число',i,'делится на', lst)
