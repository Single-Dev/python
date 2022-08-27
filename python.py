class Num:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __add__(self,  value):
        return Num(self.x + value.x, self.y - value.y)

    def __repr__(self):
        return f'X teng{self.x} Y {self.y}ga teng'


num = Num(25, 55)
num1 = Num(25, 25)

result = num + num1

print(result)




