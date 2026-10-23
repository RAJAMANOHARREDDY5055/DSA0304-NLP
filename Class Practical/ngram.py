
import random

text = "the cat sat on the mat the cat ate fish"

words = text.split()
bigrams = {}

for i in range(len(words) - 1):
    first = words[i]
    second = words[i + 1]

    if first not in bigrams:
        bigrams[first] = []

    bigrams[first].append(second)

word = "the"
result = [word]

for i in range(8):
    if word in bigrams:
        word = random.choice(bigrams[word])
        result.append(word)
    else:
        break

print("Generated Text:")
print(" ".join(result))
