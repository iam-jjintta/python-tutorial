
# 가변인자 활용
def average(*numbers):
    total = 0
    for n in numbers:
        total += n
    else:
        avg = total / len(numbers)
        return avg

avg = average(1, 2, 3, 4, 5)
print(avg)
