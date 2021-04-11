

class drob:
    def __init__(self, x, y):
        self.a = x
        self.b = y
        self.opt()
    def __str__(self):
        return f'{self.a}/{self.b}'
    def __add__(self, other):
        ch = self.a * other.b + other.a * self.b
        zn = self.b * other.b
        x = drob(ch, zn)
        x.opt()
        return x

    def __sub__(self, other):
        ch = self.a * other.b - other.a * self.b
        zn = self.b * other.b
        x = drob(ch, zn)
        x.opt()
        return x
    def opt(self):
        i = 2
        while (i <= self.b):
            if self.a % i == 0 and self.b % i ==0:
                self.a //= i
                self.b //= i
            i += 1
    def __lt__(self, other):
        x = self.a * other.b < other.a * self.b
        return x
A = drob(4,10)
print(A)
B = drob(10,250)
print(B)


C = A + B
print(C)

D = A - B
print(D)