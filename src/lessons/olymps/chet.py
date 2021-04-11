A = int(input())
B = int(input())

summ_chet = 0
summ_nechet = 0

for i in range(A,B+1):
    if i % 2 == 0:
        summ_chet += i
    else:
        summ_nechet += i

answ = summ_chet - summ_nechet
print(answ)