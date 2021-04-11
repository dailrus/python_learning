dels = 0
for i in range(1, 100):
    print(i,'=', end= "")
    for j in range(1, i+1):
        if i % j == 0:
            dels = dels + 1
            print('', j, end="")
    print('\n')
   # if dels == 2:
    #    print('- Простое', end= "")
    dels = 0