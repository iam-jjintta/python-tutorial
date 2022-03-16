
# from my_package.A import test1
from ..A import test1

def test2():
    test1.test()
    print('test3 module')
