
# 'BaseException' 클래스를 상속받은 예외 클래스 'MyException' 정의
class MyException(BaseException):
    pass

def f(x):
    # 정의한 예외 발생시키기
    raise MyException('예외 발생')

f(10)
