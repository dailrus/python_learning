for i in range(1, 100):
    dels = 0
    for j in range(1, i+1):
        ost = i % j
        if ost == 0:
            dels = dels + 1
    if dels == 2:
        print(i, end=', ')

    