class Name():
    def __init__(self, name,  lastname):
        self.name = name
        self.lastname = lastname
    def __str__(self):
        return f'Salom mening ismim {self.name} va mening familyam {self.lastname}'


class Age(Name):
    def __init__(self, name, lastname, age):
        super().__init__(name, lastname)
        self.age = age
    def __str__(self):
        text = super(Age, self).__str__()
        text += f' va mening yoshim {self.age}da'
        return text

class Phone(Age):
    def __init__(self, name, lastname, age, number):
        super().__init__(name, lastname, age)
        self.number = number
    def __str__(self):
        text1 = super(Phone, self).__str__()
        text1 += f'\nTelefon raqamim esa {self.number}'
        return text1

result = Phone('Bekzodbek', 'Tursunboyev', 16, 937142328)

print(result)
