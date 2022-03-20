
x = input('첫번째 수를 입력하세요:')
y = input('두번째 수를 입력하세요:')

try:
    x = int(x)
    y = int(y)
    z = x / y

except ZeroDivisionError as e:
    # 에러 메시지를 출력해서 확인할 수 있다.
    print(e)
    y = 1

except ValueError as e2:
    print(e2)
    print('정수를 입력해야 합니다.')
    x = 1
    y = 1

finally:
    print(f'{x} / {y} = {z}')
