
a = 1
b = 1

print('a:', a)
print('b:', b)

if a is b:
    print('a is b.')
else:
    print('a is not b.')

c = [1, 2, 3]
d = c
e = [1, 2, 3]

print('c:', c)
print('d:', d)
print('e:', e)

# is 키워드는 같은 메모리 주소값인지를 비교한다.
if c is d:
    print('c is d.')
else:
    print('c is not d.')

if c is e:
    print('c is e.')
else:
    print('e is not e.')
