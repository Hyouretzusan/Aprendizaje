test1 = "This is a test of the emergency text system"

with open("test", "wt") as fout:
    offset = 0
    size = len(test1)
    chunk = 100

    while True: 
        if offset > size:
            break
        
        fout.write(test1[offset : offset + chunk])
        offset += chunk