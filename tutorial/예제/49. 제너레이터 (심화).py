
def generator():
    yield 0
    yield 1
    yield 2

# 함수를 호출하게 되면 제너레이터 객체가 반환된다.
gen = generator()

# <class 'generator'>
print(type(gen))

for i in gen:
    print(i)

# __next__ 메서드를 통해 호출하는 경우
gen = generator()

a = gen.__next__()
print(a)

b = gen.__next__()
print(b)

c = gen.__next__()
print(c)

# 'StopIteration' 예외 발생
d = gen.__next__()
print(d)
