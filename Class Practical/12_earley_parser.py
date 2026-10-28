
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"]],
}

def earley(words):
    n = len(words)
    chart = [set() for _ in range(n + 1)]
    # State format: (lhs, tuple(rhs), dot_position, origin)
    chart[0].add(("ROOT", ("S",), 0, 0))

    for i in range(n + 1):
        changed = True
        while changed:
            changed = False
            for state in list(chart[i]):
                lhs, rhs, dot, origin = state
                if dot < len(rhs):
                    next_symbol = rhs[dot]
                    if next_symbol in grammar:  # Predict
                        for prod in grammar[next_symbol]:
                            new_state = (next_symbol, tuple(prod), 0, i)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True
                    elif i < n and words[i] == next_symbol:  # Scan
                        chart[i + 1].add((lhs, rhs, dot + 1, origin))
                else:  # Complete
                    for prev in list(chart[origin]):
                        plhs, prhs, pdot, porigin = prev
                        if pdot < len(prhs) and prhs[pdot] == lhs:
                            new_state = (plhs, prhs, pdot + 1, porigin)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True
    return ("ROOT", ("S",), 1, 0) in chart[n]

sentence = input("Enter a sentence (example: the cat sees the dog): ").strip().split()
print("Accepted" if earley(sentence) else "Rejected")
