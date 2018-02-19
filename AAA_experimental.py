surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)
last = len(surprise)-1
lastlow = surprise[last].lower()
surprise[last] = lastlow
lastrev = surprise[last][::-1]
lastcap = lastrev.capitalize()
surprise[last] = lastcap

print(surprise)