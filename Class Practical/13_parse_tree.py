
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"]],
}

def build(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and words[pos] == symbol:
            return (symbol, pos + 1)
        return None
    for production in grammar[symbol]:
        children, current = [], pos
        for item in production:
            result = build(item, words, current)
            if result is None:
                break
            child, current = result
            children.append(child)
        else:
            return ((symbol, children), current)
    return None

def display(tree, depth=0):
    if isinstance(tree, str):
        print("  " * depth + tree)
    else:
        label, children = tree
        print("  " * depth + label)
        for child in children:
            display(child, depth + 1)

words = input("Enter a sentence (example: the cat sees the dog): ").strip().split()
result = build("S", words, 0)
if result and result[1] == len(words):
    print("Parse tree:")
    display(result[0])
else:
    print("Sentence does not match the grammar.")
