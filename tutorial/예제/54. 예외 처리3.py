
file = None

try:
    file = open('test.txt')
    lines = file.readlines()
    for line in lines:
        print(line)

except FileNotFoundError as e:
    print(e)
    print('해당 파일이 존재하지 않습니다.')

finally:
    # 예외와는 상관없이 필수적으로 해줘야 하는 작업을 'finally' 절에서 해준다.
    if file:
        file.close()
