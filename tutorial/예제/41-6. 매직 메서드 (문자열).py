
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}(이)라는 사람'

    def __repr__(self):
        return f'Person({self.name}, {self.age})'


loser = Person('흔한 찐따', 28)
print(loser)
print(repr(loser))
