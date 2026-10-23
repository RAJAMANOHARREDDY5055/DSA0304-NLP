
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

text = "The smart student writes Python programs."

words = nltk.word_tokenize(text)

tags = nltk.pos_tag(words)

print("POS Tagged Words:")

for word, tag in tags:
    print(word, ":", tag)
