
import random


def lotto_numbers():
    lotto = set()
    while not len(lotto) == 6:
        lotto.add(random.randint(1, 45))
    else:
        lotto = list(lotto)
        lotto.sort()
        return list(lotto)


lotto = lotto_numbers()
print(lotto)
