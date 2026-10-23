
text = "I want to play cricket"

words = text.split()

# Initial POS tags
tags = []

for word in words:
    if word.lower() in ["I", "you", "he", "she", "we", "they"]:
        tags.append("PRON")
    elif word.lower() == "to":
        tags.append("TO")
    else:
        tags.append("NN")

# Transformation rule:
# Change the word after "to" into a verb.
for i in range(1, len(words)):
    if words[i - 1].lower() == "to":
        tags[i] = "VB"

print("Transformation-Based POS Tagging:")

for word, tag in zip(words, tags):
    print(word, ":", tag)
