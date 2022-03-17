
# 값 삭제하기

# 리스트 (list)

a = [1, 2, 3, 4, 5]
print('before:', a)

# remove 함수는 리스트에 존재하는 값을 삭제시킨다.
a.remove(1)
print('remove:', a)

# del 키워드로 삭제시킬 수도 있다.
del a[0]
print('del:', a)

# pop 함수를 사용하면 가장 마지막의 요소를 삭제시킨다.
last = a.pop()
print('last:', last)
print('pop:', a)

# 집합 (set)

b = {1, 2, 3, 4, 5}
print('before:', b)

# 리스트와는 마찬가지로 집합의 remove 함수는 해당 값을 삭제시킨다.
b.remove(3)
print('remove:', b)

# 딕셔너리 (dict)
c = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print('before:', c)

# del 키워드로 삭제시킬 수 있다.
del c['a']
print('del:', c)

# 리스트처럼 pop 함수를 사용하면 키에 해당하는 키와 값의 쌍을 삭제시킨다.
# pop 함수를 사용하면 삭제된 키에 해당하는 값이 반환된다.
b = c.pop('b')
print('b (pop):', b)
print('pop:', c)

# pop 함수의 인자값에 첫번째는 키, 두번째는 키가 존재하지 않을 경우에 반환될 값을 넣어 사용이 가능하다.
a = c.pop('a', 0)
print('a (pop):', a)
print('pop:', c)

# popitem 함수는 마지막 키와 값을 삭제하고 삭제된 키와 값의 쌍을 튜플 타입으로 반환시킨다.
last = c.popitem()
print('last (popitem):', last)
print('popitem:', c)
