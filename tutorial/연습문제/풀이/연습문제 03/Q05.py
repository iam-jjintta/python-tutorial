
# 파일 입출력을 할 경우, 반드시 close 함수를 사용해야 한다.
f1 = open('test.txt', 'w')
f1.write('Life is too short')
f1.close()

f2 = open('test.txt', 'r')
print(f2.read())
f2.close()


# with-as 문을 사용하면 이와 같은 실수를 방지할 수 있다.
with open('test.txt', 'w') as file:
    file.write('Life is too short')

with open('test.txt') as file:
    data = file.read()
    print(data)
