finger = int(input('Введите номер пальца руки (где 1 - большой, а 5 - мизинец)> '))
if 1 <= finger <= 5:
    print('Это -', end= ' ')
    if finger == 1:
        print('большой палец')
    elif finger == 2:
        print('указательный палец')
    elif finger == 3:
        print('средний палец')
    elif finger == 4:
        print('безымянный палец')
    elif finger == 5:
        print('мизинец')
else:
    print('Недопустимое значение!')