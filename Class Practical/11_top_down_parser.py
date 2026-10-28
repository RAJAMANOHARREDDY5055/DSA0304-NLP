
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"], ["John"]],
    "VP": [["V", "NP"], ["V"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["sleeps"]],
}

def parse(symbol, words, position):
    """Return possible ending positions after matching symbol at position."""
    if symbol not in grammar:  # terminal
        if position < len(words) and words[position] == symbol:
            return [position + 1]
        return []

    endings = []
    for production in grammar[symbol]:
        positions = [position]
        for item in production:
            next_positions = []
            for p in positions:
                next_positions.extend(parse(item, words, p))
            positions = next_positions
            if not positions:
                break
        endings.extend(positions)
    return endings

sentence = input("Enter a sentence (example: the cat sees the dog): ").strip().split()
print("Accepted" if len(sentence) in parse("S", sentence, 0) else "Rejected")
