import random
def count_v(n,a):
    d = {}
    x = 0
    for i in range(1, n+1):
        count = a.count(i)
        x += count
        d.update({i : count})
    for i in range(1, n+1):
        p = d[i] / x * 100
        print(i, d[i], p)

print('###### Меню ######')
print('1. Manual input')
print('2. Random auto input')
print('0. Exit')
key = int(input())
if key == 1:
    z = int(input('Введите количество выбираемых: '))
    print('Input votes: ')
    b = list(map(int, input.split(' ')))
    count_v(z, b)
elif key == 2:
    print