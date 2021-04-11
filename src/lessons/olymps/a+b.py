from os import read, write


inp = open('INPUT.TXT', mode='r')
outp = open('OUTPUT.TXT', mode='w')
lol = str(inp.read())
listik = lol.split()
a = int(listik[0])
b = int(listik[1])
outp.write(str(a+b))
print(listik)