import math
direction = 1 #Направление от 0 до 3
x = 0
y = 0
inputstr = input()
for i in range(len(inputstr)):
    if inputstr[i] == 'L':
        direction = direction - 1
    elif inputstr[i] == 'R':
        direction = direction + 1
    if direction == 0:
        x = x - 1
    elif direction == 1:
        y = y + 1
    elif direction == 2:
        x = x + 1
    elif direction == 3:
        y = y - 1
answer_raw = math.sqrt((x**2) + (y**2))
answer = int(answer_raw)
print(answer)