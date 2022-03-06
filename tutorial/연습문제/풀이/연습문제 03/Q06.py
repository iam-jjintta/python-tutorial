
data = input('저장할 데이터를 입력하세요:')

# 파일 쓰기 모드를 'a'로 지정하면 기존에 있는 데이터를 추가시키며 저장한다.
with open('test.txt', 'a') as file:
    file.write(data + '\n')
