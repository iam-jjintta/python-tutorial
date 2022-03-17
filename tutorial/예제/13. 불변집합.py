
a = frozenset([1, 2, 3, 4, 5])
b = frozenset([1, 2, 6])

print('a:', a)
print('b:', b)

print('교집합:', a & b)
print('합집합:', a | b)
print('차집합:', a - b)
