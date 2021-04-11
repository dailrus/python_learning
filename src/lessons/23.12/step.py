summ = 0

import random
a = [[random.randint(0,9) for i in range(1,11)] for j in range(1,11)]
for i in range(len(a)):
    print(a[i])
for j in range(0,len(a)):
    for k in range(j+1, len(a)):
        summ = summ + a[j][k]
        #print(j,k)
print(summ)

