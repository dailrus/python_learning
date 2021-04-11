inp_unsort = input()
if len(inp_unsort) == 2 and inp_unsort[0].isupper and inp_unsort[1].isdigit:
    inp = list(inp_unsort)
    if ord(inp[0]) / 2 == 0 and int(inp[1]) / 2 == 0:
        print('Клетка чёрная')
    if not ord(inp[0]) / 2 == 0 and not int(inp[1]) / 2 == 0:
        print('Клетка белая')
    if        
else:
    print('Ошибка ввода!')

