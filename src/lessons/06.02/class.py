class human:
    name = ''
    age = 0

    def setup(self, a, b):
        self.name = a
        self.age = b
    def print(self):
        print(self.name, self.age)


dan = human()
dan.setup('Danil', 16)
dan.print()
