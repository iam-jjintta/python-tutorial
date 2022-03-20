
x = input('첫번째 수를 입력하세요:')
x = int(x)

y = input('두번째 수를 입력하세요:')
y = int(y)

# 'y'가 '0'이면 '1'을 대입시킨다.
if y == 0:
    y = 1

z = x / y
print(f'{x} / {y} = {z}')
