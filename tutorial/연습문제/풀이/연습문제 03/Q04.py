
# youneedpython
print('you' 'need' 'python')
# youneedpython
print('you' + 'need' + 'python')
# you need python
print('you', 'need', 'python')
# youneedpython
print("".join(['you', 'need', 'python']))

# 결과
# youneedpython
# youneedpython
# you need python
# youneedpython

# 이유
# 1. 단순히 문자열을 나열한 것과 같다.
# 2. 문자열을 합친 것이다.
# 3. print 함수는 가변인자로 값을 넘길 경우, 기본적으로 띄어쓰기가 적용된다.
# 4. join 함수를 통해 문자열을 합치는데 join을 통해 합쳐지는 문자열이 빈 문자열이다.
