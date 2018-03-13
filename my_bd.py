from datetime import date, timedelta
import time

bdC = date(1987, 8, 10)
print(bdC)

thousand_10 = timedelta(days=10000)
tdC = bdC + thousand_10
print("I was 10000 days old in:", tdC)