class Phone:
    manufact = None
    model = None
    number = None
    def set(self, a, b ,c):
        self.manufact = a
        self.model = b
        self.number = c
    def print(self):
        print(self.manufact, self.model, self.number)
    def recieveCall(self, name):
        print(f'На телефон {self.manufact}{self.model} звонит {name}')
    
