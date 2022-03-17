
# 새로운 클래스 'MyClass' 정의
class MyClass:
    # 클래스 변수 'a'
    a = 1

    # 생성자 정의
    def __init__(self):
        # 인스턴스 변수 'a'
        self.a = 10


# 클래스 변수 'a'를 의미한다.
print(MyClass.a)

# 새로운 객체 'my_class' 인스턴스화
my_class = MyClass()
# 새롭게 생성된 객체 'my_class'의 변수 'a'를 의미한다.
print(my_class.a)

# 새로운 객체 'my_class2' 인스턴스화
my_class2 = MyClass()
# 새롭게 생성된 객체 'my_class'의 변수 'a'의 값을 '20'으로 변경
my_class2.a = 20

# '10'이 출력된다.
print(my_class.a)
# '20'이 출력된다.
print(my_class2.a)
