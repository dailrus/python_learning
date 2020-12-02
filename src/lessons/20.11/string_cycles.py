print('Введите строку')
string = input()
# cat = 'привет'

out = ''

for i in reversed(range(len(string))):
    out = out + string[i]
print(out, type(out))
out_int = int(out)
print(out_int, type(out_int))

    