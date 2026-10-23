
import re

text = "The happy boy runs quickly"

words = text.split()

patterns = [
    (r".*ly$", "RB"),
    (r".*ing$", "VBG"),
    (r".*ous$", "JJ"),
    (r".*s$", "NNS"),
]

print("Rule-Based POS Tagging:")

for word in words:
    tag = "NN"

    if word.lower() in ["the", "a", "an"]:
        tag = "DT"
    elif word.lower() in ["is", "am", "are", "was", "runs"]:
        tag = "VB"
    else:
        for pattern, pos in patterns:
            if re.fullmatch(pattern, word.lower()):
                tag = pos
                break

    print(word, ":", tag)
