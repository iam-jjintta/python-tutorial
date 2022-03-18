
class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    # getter 메서드
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # setter 메서드
    def set_name(self, name):
        # 이름은 문자열 타입으로 바꿔서 지정해준다.
        self._name = str(name)

    def set_age(self, age):
        # 나이는 정수 타입으로 바꿔서 지정해준다.
        self._age = int(age)
        # 음의 정수는 사용이 불가능하도록 해준다.
        if self._age < 0:
            self._age = 0


me = Person('흔한 찐따', 28)
print(me.get_name())
print(me.get_age())

me.set_name('안 흔한 찐따')
print(me.get_name())

# 음의 정수인 경우, 0이 된다.
me.set_age(-10)
print(me.get_age())

# 아래를 실행하려고 하면 int 타입이 아니므로 에러가 발생하게 된다.
me.set_age('뭘까요...?')
print(me.get_age())
