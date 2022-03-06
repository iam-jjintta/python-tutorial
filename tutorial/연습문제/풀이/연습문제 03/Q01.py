
# 1. def 키워드를 통해 함수 정의
def is_odd(x):
    return x % 2 == 0

print(is_odd(2))

# 2. lambda 키워드를 통해 람다 함수 정의
is_odd = lambda x: x % 2 == 0

print(is_odd(3))
