
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = [
    "playing",
    "played",
    "plays",
    "connected",
    "connection",
    "happiness",
    "studies",
    "running"
]

print("Porter Stemming")
print("---------------")

for word in words:
    stem = stemmer.stem(word)
    print(word, "->", stem)
