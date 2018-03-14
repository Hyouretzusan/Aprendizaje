import time

today_string = ""
with open ("today.txt", "rt") as din:
    for date in din:
    	today_string += date

print(today_string)