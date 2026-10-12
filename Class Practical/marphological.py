
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

lemmatizer = WordNetLemmatizer()

words = ["cars", "playing", "studies", "better", "mice"]

print("Morphological Analysis")
print("----------------------")

for word in words:
    noun_form = lemmatizer.lemmatize(word, pos='n')
    verb_form = lemmatizer.lemmatize(word, pos='v')
    adjective_form = lemmatizer.lemmatize(word, pos='a')

    print("Word:", word)
    print("  Noun lemma:", noun_form)
    print("  Verb lemma:", verb_form)
    print("  Adjective lemma:", adjective_form)
