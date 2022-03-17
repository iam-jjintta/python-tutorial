
a = {1, 2, 3}
print('a:', a)
print('type:', type(a))

a2 = set([1, 2, 3])
print(a2)

# 집합은 인덱싱이 불가능하므로 아래와 같은 에러가 발생한다.
# TypeError: 'set' object is not subscriptable
b = a[0]
print(b)

# 집합을 인덱싱하기 위해서는 리스트나 튜플로 변형시켜야 한다.
a3 = list(a)
b = a[0]
print(b)

a4 = tuple(a)
b2 = a4[1]
print(b2)
