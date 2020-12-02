n = 0 
summ = 0
for i in range(999):
    n = i
    summ = 0
    while n > 0:
        summ = summ + (i % 10)
        n = i // 10
        if summ == i:
            print(i)
        else:
            print('fuck {0}'.format(i))
            break
