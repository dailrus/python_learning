inp_1 = int(input('Введите первое целое число: '))
inp_2 = int(input('Введите второе целое число: '))

if inp_1 < inp_2:
    answer = inp_1 + inp_2
    print('Сумма чисел =', answer)
elif inp_2 < inp_1:
    answer = inp_1 - inp_2
    print('Разность чисел =', answer)

elif inp_1 == inp_2:
    print('Числа равны, действий не требуется!')