
class Dog:
    def berk(self):
        print('멍멍!')


class Maltese(Dog):
    def berk(self):
        print('왕왕!')

d = Dog()
m = Maltese()
dogs = [d, m]

for dog in dogs:
    dog.berk()
