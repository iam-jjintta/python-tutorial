
# 가변인자
def f(*args):
    print('가변인자 args의 값:', args)
    print('가변인자 args의 타입:', type(args))


f(1, 2, 3)

# 키워드 파라미터
def f2(**kwargs):
    print('키워드 파라미터 kwargs의 값:' kwargs)
    print('키워드 파라미터 kwargs의 타입:', type(kwargs))


# 사용하는 방법은 다음과 같이 매개변수=값 형식으로 호출하여 사용한다.
f2(a=1, b=2)

# 둘 다 사용하기
def f3(a, b=1, *args, **kwargs):
    # 키워드 파라미터의 키(key)값이 어떤 키가 될지 모르니 get 함수를 사용하는 것이 좋다.
    x = kwargs.get('x', 0)
    y = kwargs.get('y', 0)

    for i in args:
        x = x + i
    else:
        result = y + (x * a) + b
        return result


# a의 값은 1
# b의 값은 2
# args의 값은 (3, 4)
# kwargs의 값은 {'x': 10, 'y': 20}
y = f3(1, 2, 3, 4, x=10, y=20)
print(y)
