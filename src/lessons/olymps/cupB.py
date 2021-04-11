

t = int(input())
lst = []
while not t == 0:
    fake = False
    numb = int(input())
    #while not fake == True:
    for g in range(numb, numb+999999999):
        lst = list(map(int, str(g)))
        for j in range(0, len(lst)):
            if lst[j] == 0:
                    lst.remove(0)
        for k in range(0, len(lst)):
            if not lst[k] == 0:
                if not g % lst[k] == 0:
                    fake = True
                
        if fake == False:
            print(g)
            lst.clear
            break
    
    
            




    t -= 1