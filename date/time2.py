import time

#t = time.time()
t  = time.localtime()
currentTime = time.strftime("%H:%h:%M:%S", t)
print(currentTime)