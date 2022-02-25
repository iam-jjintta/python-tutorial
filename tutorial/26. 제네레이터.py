
# 튜플을 컴프리헨션을 하면 제네레이터 타입이 된다.
y = (x for x in range(1, 3))
print('y:', y)
print(type(y))

# next 함수를 사용해서 첫번째 값부터 차례대로 불러낸다.
# next 함수를 통해 값을 가져오면 제네레이터의 첫번째 값은 삭제되며, 메모리에서 해제된다.
n = next(y)
print('next:', n)
n2 = next(y)
print('next:', n2)
# 만약 더 이상 불러올 값이 존재하지 않는다면 StopIteration 에러가 발생한다.
# n3 = next(y)
# print('next:', n3)

# for 문 사용 시 모든 값들을 불러낼 수 있다.
gen = (x for x in range(1, 11))
for i in gen:
    print('i:', i)
