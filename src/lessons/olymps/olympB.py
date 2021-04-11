# N <= 10^9
for i in range(100000):
    delitls = 0
    for j in range(1, i+1):
        if i % j == 0:
            delitls = delitls + 1
    if delitls == 5:
        print(i)