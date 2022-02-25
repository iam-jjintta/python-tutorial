
a = [1, 2, 3]
b = a
c = [1, 2, 3]

if a == b:
    print('a is same to b.')
elif a != b:
    print('a is not same to b.')

if a == c:
    print('a is same to c.')
elif a != b:
    print('a is not same to c.')

if b == c:
    print('b is same to c.')
elif b != c:
    print('b is not same to c.')

if a and b:
    print('a and b is True.')
else:
    print('a and b is False.')

if a and c:
    print('a and b is True.')
else:
    print('a and b is False.')
