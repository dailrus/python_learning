#Расчёт Яблок, Груш, БАпельсинов

import random

budget = random.randint(1000, 50000)

print('Введите стоимость яблок')
apple_cost = input(int)
print('Введите количество яблок')
apple_count = input(int)

remain = budget - (apple_cost * apple_count)

x = remain/3

print('Введите стоимость груш')
apple_cost = input(int)