
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

# 10에서 7을 뺀 3을 출력한다.
print(cal.value)
