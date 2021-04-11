t = int(input())
scob = 0
other = 0

while not t == 0:
    n = int(input())
    inp = input()
    other = n//2
    scob = 0
    for i in reversed(range(0, n)):
        if inp[i] == ')':
            scob +=1
        else:
            break
    if scob > other:
        print('Yes')
    else:
        print('No')

    t -= 1