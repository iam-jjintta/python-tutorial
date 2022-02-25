
x = []
for i in range(1, 101):
    x.append(i)
else:
    # sum 함수는 모든 값들을 한번에 더해주는 함수이다.
    result = sum(x)
    print(result)

# 다중 반복문
for i in range(1, 11):
    print('i:', i)
    for j in range(1, 11):
        print('j:', j)
    print('---------')
