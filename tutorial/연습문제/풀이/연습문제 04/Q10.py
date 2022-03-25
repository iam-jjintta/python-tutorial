
import os

os.chdir('C:/Users/iamjjintta/study')
with os.popen('dir') as result:
    print(result.read())
