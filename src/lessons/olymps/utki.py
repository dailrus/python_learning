A = int(input())
B = int(input())
flag = False
answ = max(A, B)

while not flag == True:
    answ += 1 
    if answ % A == 1 and (answ+1) % B == 0:
        flag = True


print(answ)