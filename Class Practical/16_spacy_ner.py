

import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Model missing. Run: python -m spacy download en_core_web_sm")
    raise SystemExit(1)

text = input("Enter text: ").strip()
doc = nlp(text)

print("\\nNamed entities:")
if not doc.ents:
    print("No named entities found.")
for ent in doc.ents:
    print(f"{ent.text:25} {ent.label_:10} {spacy.explain(ent.label_)}")
