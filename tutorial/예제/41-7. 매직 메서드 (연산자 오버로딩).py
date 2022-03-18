class Room:
    def __init__(self, people=[]):
        self.people = people

    def __str__(self):
        return f'총 인원수: {len(self.people)}'

    def __add__(self, person):
        self.people.append(person)
        print(person, '님이 입장하셨습니다.')
        return Room(self.people)

class Person:
    def __init__(self, name):
        self.name = str(name)

    def __str__(self):
        return self.name


room = Room()

p1 = Person('흔한 찐따')
p2 = Person('안 흔한 찐따')

room = room + p1
room = room + p2

print(room)