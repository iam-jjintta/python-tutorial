
class Room:
    def __init__(self, people=[]):
        self.people = people

    def __str__(self):
        return f'총 인원수: {len(self)}'

    def __add__(self, person):
        self.people.append(person)
        print(person, '님이 입장하셨습니다.')
        return Room(self.people)

    def __len__(self):
        return len(self.people)

    def __getitem__(self, i):
        return self.people[i]

    def __setitem__(self, i, person):
        self.people[i] = person
        print(i, '번째 방에', person, '님이 입장하셨습니다.')

    def __delitem__(self, i):
        out = self.people.pop(i)
        print(out, '님이 퇴장하셨습니다.')

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
print(room[0])

del room[0]

print(room)
print(room[0])

p3 = Person('희귀한 찐따')
room[0] = p3
print(room)
