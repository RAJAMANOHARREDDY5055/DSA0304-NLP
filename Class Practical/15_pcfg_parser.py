
grammar = {
    "S": [(["NP", "VP"], 1.0)],
    "NP": [(["Det", "N"], 0.7), (["Name"], 0.3)],
    "VP": [(["V", "NP"], 0.6), (["V"], 0.4)],
    "Det": [(["the"], 1.0)],
    "N": [(["cat"], 0.5), (["dog"], 0.5)],
    "V": [(["sees"], 0.6), (["sleeps"], 0.4)],
    "Name": [(["John"], 1.0)],
}

def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and words[pos] == symbol:
            return [(pos + 1, 1.0, symbol)]
        return []
    results = []
    for rhs, rule_prob in grammar[symbol]:
        partials = [(pos, rule_prob, [])]
        for item in rhs:
            updated = []
            for p, prob, children in partials:
                for end, child_prob, child_tree in parse(item, words, p):
                    updated.append((end, prob * child_prob, children + [child_tree]))
            partials = updated
        for end, prob, children in partials:
            results.append((end, prob, (symbol, children)))
    return results

words = input("Enter a sentence (example: the cat sees the dog): ").strip().split()
parses = [(end, prob, tree) for end, prob, tree in parse("S", words, 0) if end == len(words)]
if parses:
    end, probability, tree = max(parses, key=lambda x: x[1])
    print("Most probable parse:", tree)
    print("Probability:", round(probability, 6))
else:
    print("No valid parse found.")
