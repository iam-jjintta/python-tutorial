
def generator():
    yield 1
    yield 2
    return '더 이상 값이 존재하지 않습니다.'
 
# 제너레이터 생성
gen = generator()

# 'next' 함수를 통해 다음 값을 꺼내온다.
next(gen)
next(gen)

# 아래의 코드가 실행될 경우, 'StopIteration: 더 이상 값이 존재하지 않습니다.' 라는 메시지가 출력된다.
next(gen)
