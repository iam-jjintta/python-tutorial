
def outer():
    print("외부 함수 영역")
    a = 10

    # 내부 함수 'inner' 호출
    def inner():
        print("내부 함수 영역")

        # nonlocal 키워드를 사용하여 함수 'outer' 영역에 선언된 변수 'a'를 사용하겠다는 의미이다.
        nonlocal a
        a += 10
        print('a:', a)

    # 내부 함수 'inner' 호출
    inner()

# 함수 'outer' 호출
outer()
