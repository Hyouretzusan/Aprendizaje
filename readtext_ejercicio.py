test2 = ""
with open("test", "rt") as fhandle:
    for lines in fhandle:
        test2 = test2 + lines
    print(test2)