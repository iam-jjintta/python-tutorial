
with open('test.txt') as file:
    data = file.read()

# replace를 통해 불러온 데이터 중 'java'라는 문자열을 'python'으로 변경해준다.
data = data.replace('java', 'python')
with open('test.txt', 'w') as file:
    file.write(data)
