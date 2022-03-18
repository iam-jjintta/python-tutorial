
class A:
    a = 10

    def test(self):
        print('클래스 A')

class B(A):
    a = 20

    def test(self):
        super().test()

a = A()
b = B()

# '클래스 A'가 출력된다.
a.test()
# '클래스 A'가 출력된다.
b.test()
