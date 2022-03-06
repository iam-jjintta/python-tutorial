
# 파일 쓰기
data = 'Hello, Python!'

file = open('test.txt', 'w')
file.write(data)
file.close()

# with-as 문으로 파일 쓰기
data2 = '안녕, 파이썬!'

with open('test.txt', 'w') as file:
    file.write(data2)
