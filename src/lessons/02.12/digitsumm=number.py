# от 1 до 1000, у которых сумма цифр равна числу
for i in range(1, 1000):
    lst = []
    summ = 0
    for j in range(1, i+1):
        ost = i % j
        if ost == 0:
            summ = summ + j
            lst.append(j)
            #print('Число',i,'делится на', lst)
    if summ == i:
        print(i)
   # for i in range(len(lst)):
   #    summ = summ + lst[i]
   # if i == summ:
   #     print(i)