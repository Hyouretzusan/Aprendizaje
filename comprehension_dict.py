#{key: value for value in iterable if condición} If opcional
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)