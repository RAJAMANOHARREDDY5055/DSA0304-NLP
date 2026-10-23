
text = "I love Python"

probabilities = {
    "I": {"PRON": 0.9, "NOUN": 0.1},
    "love": {"VERB": 0.8, "NOUN": 0.2},
    "Python": {"NOUN": 0.9, "VERB": 0.1}
}

words = text.split()

print("Stochastic POS Tagging:")

for word in words:
    if word in probabilities:
        tag = max(
            probabilities[word],
            key=probabilities[word].get
        )
    else:
        tag = "UNKNOWN"

    print(word, ":", tag)
