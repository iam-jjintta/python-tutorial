
# 문자열 (str) 타입 역시 여러 문자 타입이 나열된 타입이므로, 컨테이너 (Container) 타입이다.
# 선언 시 작은 따옴표 혹은 큰 따옴표로 선언한다.
a = 'Hello'
b = "Python!"

print(a, ',', b)

# str 함수를 통해 선언할 수도 있다.
s = str('Hello, Python!')
print(s)

# 다른 타입을 문자열로 바꾸는 것이 가능하다.
n = 10
s = str(n)
print('s:', s)
print(type(s))

# del 키워드는 사용할 수 없다.
# 만약 del 키워드로 문자 하나를 제거하려고 할 경우, 아래와 같은 에러가 발생한다.
# TypeError: 'str' object doesn't support item deletion
a = 'Hello'
# del a[0]
print(a)

# 문자열도 덧셈 연산이 가능하다.
c = a + ', ' + b
print(c)

# 문자열도 인덱싱과 슬라이싱이 가능하다.
d = c[0]
e = c[0:5]
print('d:', d)
print('e:', e)
