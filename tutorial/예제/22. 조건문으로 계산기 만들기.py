
# input 함수로 값을 입력할 수 있다.
a = input('첫번째 수를 입력하세요:')
op = input('연산자를 입력하세요:')
b = input('두번째 수를 입력하세요:')

# 그냥 실행하면 에러가 나서 정수 타입으로 변환시켜야 한다.
a = int(a)
b = int(b)

if op == '+':
    print(a, op, b, '=', a + b)
elif op == '-':
    print(a, op, b, '=', a - b)
elif op == '*':
    print(a, op, b, '=', a * b)
elif op == '/':
    print(a, op, b, '=', a / b)
elif op == '**':
    print(a, op, b, '=', a ** b)
elif op == '//':
    print(a, op, b, '=', a // b)
elif op == '%':
    print(a, op, b, '=', a % b)
