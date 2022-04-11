
import json


# 결과: '["\ud754\ud55c\ucc10\ub530", {"\ucc10\ub530": ["\uc548\ub155\ud558\uc138\uc694", null, 1.0, 2]}]'
a = json.dumps(['흔한찐따', {'찐따': ('안녕하세요', None, 1.0, 2)}])
print(a)

# 결과: "\"\ud754\ud55c\ucc10\ub530\\\ucc10\ub530"
print(json.dumps("\"흔한찐따\찐따"))

# 결과: "\u1234"
print(json.dumps('\u1234'))

# 결과: "\\"
print(json.dumps('\\'))

# 결과: {"a": 0, "b": 0, "c": 0}
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))


with open('test.json', 'w', encoding='utf8') as file:
    file.write(a)

# 'test.json' 불러오기
with open('test.json') as file:
    data = json.load(file)
    # 결과: ['흔한찐따', {'찐따': ['안녕하세요', None, 1.0, 2]}]
    print(data)
