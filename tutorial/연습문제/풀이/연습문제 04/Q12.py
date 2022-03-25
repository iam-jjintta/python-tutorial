
import time

t = time.time()
localtime = time.localtime(t)
print(time.strftime('%Y/%m/%d %X', localtime))
