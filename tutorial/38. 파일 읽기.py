
# 파일 읽기

# 1. readline 함수
with open('test.txt') as file:
    while True:
        line = file.readline()
        # 더 이상 불러올 데이터(라인)이 없는 경우, 반복문을 빠져 나온다.
        if line is None:
            break
        print(line)

# 2. readlines 함수
with open('test.txt') as file:
    lines = file.readlines()

    for line in lines:
        print(line)

# 3. read 함수
with open('test.txt') as file:
    data = file.read()
    print(data)
