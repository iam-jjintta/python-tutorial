
# 문자열 포맷팅(Formatting)

# 숫자 대입하기
s = 'I eat %d apples.' % 3
print(s)

# 문자열 대입
s2 = 'I eat %s apples.' % 'five'
print(s2)

# 숫자 값을 나타내는 변수로 대입
n = 3
s3 = 'I eat %d apples.' % n
print(s3)

# 2개 이상의 값 넣기
n2 = 10
ss = 'three'
s4 = 'I ate %d apples. so I was sick for %s days.' % (n2, ss)
print(s4)

# format 함수를 사용한 포매팅
n3 = 10
s5 = 'I ate {0} apples.'.foramt(n3)
print(s5)

# format 함수로 여러 값들을 대입하기
n4 = 11
n5 = 10
s6 = '{0} is bigger than {1}.'.format(n4, n5)
print(s6)
