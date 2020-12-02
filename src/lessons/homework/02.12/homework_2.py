import random
a, b, c = random.randint(-50, 50), random.randint(-50, 50), random.randint(-50, 50), 

if a <= b <= c:
    print('Квадраты чисел')
    a = a**2
    b = b**2
    c = c**2
elif a > b > c:
    print('Наибольшее число')
    b = a 
    c = a
else:
    print('Действий не произведено')
print('a = {0}\nb = {1}\nc = {2}'.format(a,b,c))




