import time

now = time.time()
strToday = time.ctime(now)

with open ("today.txt", "wt") as dout:
    dout.write(strToday)