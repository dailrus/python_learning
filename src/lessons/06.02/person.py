class Person():
    name = 'Иван'
    surname = 'Иванов'
    patronymic = 'Иванович'
    age = 45

    def talk(self, msg):
        print(self.surname, self.name, self.patronymic,f'говорит: "{msg}"')
    def set(self, name, surname, pat, age):
        self.name = name
        self.surname = surname
        self.patronymic = pat
        self.age = age
    def Rename(self, name):
        self.name = name
    def getyear(self):
        return(2021- self.age)

dan = Person()
dan.set('Данил', 'Офицеров', 'Андреевич', 17)
dan.talk('Привет, мир!')
dan.Rename('Дэнчик')
print(f'Теперь ты {dan.name}, ха-ха')
dan.talk('Вообще-то обидно')
print(f'Он родился в {dan.getyear()} году, типичный школьник =)')
