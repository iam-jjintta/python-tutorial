
# 값 수정하기

# 리스트 (list)

a = [1, 2, 3, 4, 5]
print('before:', a)

a[0] = 6
print('after:', a)

# 집합 (set)

b = {1, 2, 3, 4, 5}
print('before:', b)

# 리스트 타입으로 변형시킨 뒤에 요소를 수정해야 한다.
b2 = list(b)
b2[0] = 6
b = set(b2)
print('after:', b)

# 딕셔너리 (dict)

c = {'a': 1, 'b': 2, 'c': 3}
print('before:', c)

c['a'] = 4
print('after:', c)
