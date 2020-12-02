#Расчёт Яблок, Груш, Апельсинов

# У Васи было N рублей (N задается случайным образом). Он решил потратить их на
# покупку фруктов: апельсинов, груш и яблок. Цены на фрукты необходимо спросить у
# пользователя (они вводятся с клавиатуры). Количество яблок тоже вводится с
# клавиатуры. Необходимо найти, сколько груш сможет купить Вася,
# если он купит их вдвое больше, чем апельсинов
import random

budget = random.randint(1000, 50000)
print('Ваш бюджет', budget)
print()

print('Введите стоимость яблок')
apple_cost = int(input())
print('Введите стоимость груш')
peer_cost = int(input())
print('Введите стоимость апельсинов')
orange_cost = int(input())

print('Введите количество яблок')
apple_count = int(input())

remain = budget - (apple_cost * apple_count)

x = remain/((2*peer_cost) + orange_cost)

print('У вас останется после яблок', remain)
print('Вы можете купить', x, 'груш.')
print('Вы можете купить', 2*x, 'апельсинов.')

#peer_budget = x * peer_cost
#orange_budget = 2*x * orange_cost

#remain = (2*x * peer_cost) + (x * orange_cost)