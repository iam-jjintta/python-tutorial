
# range는 첫번째 값부터 n-1까지 규칙성을 가진 값을 갖는다.

x = [i for i in range(1, 10)]
print('x:', x)

start = 1
end = 10 + 1
r = range(start, end)
a = [i for i in r]

print('a:', a)
print(type(a))

# 조건식을 사용해서 짝수만 넣기
b = [x for x in r if x % 2 == 0]
print('b:', b)

# 두 가지 값을 튜플로 한번에 넣기
c = [(x, y) for x in ['a', 'b', 'c'] for y in [1, 2, 3]]
print('c:', c)
