
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
a[[1]] = 'python'
print(a)
# 에러가 발생하지 않음
a[250] = 'python'
print(a)
