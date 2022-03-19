
s = 'abc'
i = iter(s)

# <class 'str_iterator'>
print(type(i))

a = next(i)
print(a)

b = next(i)
print(b)

c = next(i)
print(c)

# 더 이상 요소가 없으므로, 'StopIteration' 예외가 발생한다.
d = next(i)
print(d)
