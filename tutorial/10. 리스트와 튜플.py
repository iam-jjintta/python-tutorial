
l = [1, 2, 3]
t = (1, 2, 3)

print('l:', l)
print('t:', t)

# 리스트는 값을 변경할 수 있다.
l[0] = 4
print('l:', l)

# 튜플은 값을 변경할 수 없기 때문에 아래처럼 에러가 발생한다.
# TypeError: 'tuple' object does not support item assignment
t[0] = 4
print('t:', t)
