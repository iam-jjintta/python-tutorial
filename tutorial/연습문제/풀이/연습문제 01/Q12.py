
a = b = [1, 2, 3]
a[1] = 4
print(b)

# 결과: [1, 4, 3] 이 출력된다.
# 이유: a와 b는 같은 id 값을 가지기 때문에 a의 값이 바뀌면 b의 값도 같이 바뀐다.
#       따라서 is 키워드로 a와 b를 비교해보면 값이 True로 출력된다.

print(a is b)
print(id(a))
print(id(b))
