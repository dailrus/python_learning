n, m, plitki = [int(x) for x in input().split()]
count = 0
perimetr = 2*(n+m)
#perimetr_small = 2*(n-1+m-1)
#print(perimetr)
#print(perimetr_small)
otvet = 0
perimetr_current = perimetr - 4
while count <= plitki:
    count = count + perimetr_current
    perimetr_current = perimetr_current - 8
    if count <= plitki:
        otvet = otvet + 1
    else:
        break    

print(otvet)   

#for i in range():
    