
def coroutine():
    while True:
        # 함수 외부에서 값을 받아온다.
        # 값을 받아오려면 '변수명 = (yield)' 와 같이 선언한다.
        x = (yield)
        print('받아온 값:', x)


cor = coroutine()
# 제너레이터를 사용할 때 'next' 함수를 통해 다음 값을 불러왔다.
# 코루틴은 'next' 함수를 통해 초기화 작업을 진행한다.
next(cor)

# 'send' 메서드를 통해 값을 보낸다.
cor.send(10)
cor.send('안녕하세요.')
cor.send('흔한 찐따입니다.')
cor.send(3.14)
