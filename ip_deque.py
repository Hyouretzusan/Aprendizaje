from collections import deque

def palindromo(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

palabra = palindromo("arepera")
print(palabra)