
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total = total + score
else:
    # 리스트의 전체 길이를 구하는 len 함수를 응용하였다.
    avg = total / len(A)
    print('평균:', avg)
