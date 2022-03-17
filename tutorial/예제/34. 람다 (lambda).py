
# 람다(lambda)
f = lambda x1, x2: x1 + x2
y = f(3, 4)

# 타입은 lambda 타입이 나온다.
print(type(f))
print(y)

# 결과적으로 위의 코드와 동일하다.
def f(x1, x2):
    return x1 + x2

y = f(3, 4)
print(y)
