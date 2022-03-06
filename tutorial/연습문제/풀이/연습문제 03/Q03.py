
input1 = input('첫번째 숫자를 입력하세요:')
input2 = input('두번째 숫자를 입력하세요:')

# input 함수를 통해 값을 입력하면 결과는 str 타입이다.
# str 타입끼리 더하면 문자열이 합쳐진다.
# 때문에 계산한 결과값을 얻으려면 int 함수를 통해 str 타입을 int 타입으로 변환시켜야 한다.

n1 = int(input1)
n2 = int(input2)
total = n1 + n2
print('두 수의 합은 %s 입니다' % total)
