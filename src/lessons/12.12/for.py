a = [[i*j for j in range(1,11)] for i in range(1,11) ]
print(a)
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end = " ")
    print()
