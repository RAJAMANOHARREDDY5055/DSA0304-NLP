
import re
import nltk
from nltk.corpus import wordnet as wn

def words(text):
    return set(re.findall(r"[a-z]+", text.lower()))

def lesk(context, target):
    context_words = words(context) - {target.lower()}
    best_synset, best_score = None, -1
    for syn in wn.synsets(target):
        signature = words(syn.definition())
        for example in syn.examples():
            signature |= words(example)
        for lemma in syn.lemma_names():
            signature |= words(lemma.replace("_", " "))
        score = len(context_words & signature)
        if score > best_score:
            best_synset, best_score = syn, score
    return best_synset, best_score

context = input("Enter a sentence containing an ambiguous word: ").strip()
target = input("Enter the target word (must appear in the sentence): ").strip()
try:
    result, score = lesk(context, target)
    if result:
        print("Selected sense:", result.name())
        print("Definition:", result.definition())
        print("Overlap score:", score)
    else:
        print("No WordNet senses found for that word.")
except LookupError:
    print("WordNet data is missing. Run:")
    print("import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')")
