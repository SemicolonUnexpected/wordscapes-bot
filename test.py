import word_gen

print(w := word_gen.get_possibilities("abc"))

for word in w:
    print(word in word_gen.words)


