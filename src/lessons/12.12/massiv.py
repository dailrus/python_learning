import random
mass = [[random.randint(1,11), random.randint(1,11)] for i in range(1,11)]
a = int(input())
b = int(input())
print(mass[a][b])