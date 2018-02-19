e2f = {"dog":"chien", "cat":"chat", "walrus":"morse"}
#print(e2f["walrus"])

f2e = {}
tuplist = e2f.items()
for k, v in tuplist:
    nuevatup = (v, k)
    f2e[v] = k

#print(f2e["chien"])
print(set(e2f))