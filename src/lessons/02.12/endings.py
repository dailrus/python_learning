inp = int(input('Введите число от 0 до 9: '))

if 0<=inp<=9:
    if inp == 2 or inp == 3 or inp == 4:
        print(inp, 'доллара')
    elif inp == 1:
        print(inp, 'доллар')
    else:
        print(inp, 'долларов')
else:
    print('Число не входит в диапазон')