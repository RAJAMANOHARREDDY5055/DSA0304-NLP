
import nltk
from nltk.corpus import wordnet as wn

try:
    word = input("Enter a word (example: bank): ").strip()
    synsets = wn.synsets(word)
    if not synsets:
        print("No synsets found.")
    for syn in synsets:
        print("\\nSynset:", syn.name())
        print("Part of speech:", syn.pos())
        print("Definition:", syn.definition())
        print("Examples:", syn.examples() or "None")
        print("Lemmas:", ", ".join(syn.lemma_names()))
except LookupError:
    print("WordNet data is not installed. Run these commands:")
    print("import nltk")
    print("nltk.download('wordnet')")
    print("nltk.download('omw-1.4')")
