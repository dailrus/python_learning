inp_1 = int(input('Введите первое целое число> '))
inp_2 = int(input('Введите второе целое число> '))
user_answer = int(input('Введите произведение этих чисел> '))

correct_answer = inp_1 * inp_2
if user_answer == correct_answer:
    print('Ответ верный!')
else:
    print('Неверно!\nПравильный ответ - {}'.format(correct_answer))