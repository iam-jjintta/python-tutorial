
def generator():
    # 계속 참이 성립되므로, 무한 루프가 성립된다.
    x = 0
    while True:
        x += 1
        yield x

gen = generator()

# 'next' 함수를 통해 계속해서 값을 불러와도 'StopIteration' 예외가 발생되지 않는다.
a = next(gen)
print(a)

b = next(gen)
print(b)

c = next(gen)
print(c)

d = next(gen)
print(d)
