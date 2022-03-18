
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = str(name)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = int(age)
        if self._age < 0:
            self._age = 0


me = Person('흔한 찐따', 28)
print(me.name)
print(me.age)

me.name = '안 흔한 찐따'
print(me.name)

# 음의 정수인 경우, 0이 된다.
me.age = -10
print(me.age)

# 아래를 실행하려고 하면 int 타입이 아니므로 에러가 발생하게 된다.
me.age = '뭘까요...?'
print(me.age)
