
result = 0
i = 1

while i <= 1000:
    if i % 3 == 0:
        result = result + i
    i = i + 1
else:
    print('1부터 1000까지 3의 배수 합:', result)
