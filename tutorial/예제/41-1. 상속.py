
class A:
    a = 10

    def test(self):
        print('클래스 A')

class B(A):
    a = 20

    def test(self):
        print('클래스 B')

a = A()
b = B()

# '10'이 출력된다.
print('클래스 A의 멤버 변수 a:', a.a)
# '20'이 출력된다.
print('클래스 B의 멤버 변수 b:', b.a)

# '클래스 A'가 출력된다.
a.test()
# '클래스 B'가 출력된다.
b.test()
