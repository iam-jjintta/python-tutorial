
def coroutine():
    y = 0
    while True:
        x = (yield y)
        print('코루틴 호출:', x)
        y += x


cor = coroutine()
cor.send(None)

# '1'가 출력된다.
x = cor.send(1)
print('x:', x)

# '3'이 출력된다.
x = cor.send(2)
print('x:', x)

# '6'가 출력된다.
x = cor.send(3)
print('x:', x)

# '10'이 출력된다.
x = cor.send(4)
print('x:', x)
