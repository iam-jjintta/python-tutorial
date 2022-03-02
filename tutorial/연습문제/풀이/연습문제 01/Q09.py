
a = dict()

# 에러가 발생하지 않음
a['name'] = 'python'
print(a)
# 에러가 발생하지 않음
a[('a',)] = 'python'
print(a)
# 에러 발생: 리스트 타입은 키(key)가 될 수 없음
# 실행하면 아래와 같은 에러가 발생함
# TypeError: unhashable type: 'list'
# 상세 이유:
# 딕셔너리 타입의 키(key)는 "변하지 않는 고유한 값"이어야 한다.
# 리스트 타입은 "변할 수 있는" 값이기 때문에 키(key)가 될 수 없다.
a[[1]] = 'python'
print(a)
# 에러가 발생하지 않음
a[250] = 'python'
print(a)
