
def plural_fsm(noun):
    # State 0: Read the noun
    state = 0

    # State 1: Apply the plural rule
    if noun.endswith(("s", "sh", "ch", "x", "z")):
        state = 1
        plural = noun + "es"

    elif noun.endswith("y") and len(noun) > 1:
        if noun[-2].lower() not in "aeiou":
            state = 2
            plural = noun[:-1] + "ies"
        else:
            state = 1
            plural = noun + "s"

    else:
        state = 1
        plural = noun + "s"

    # Final state: Return the plural form
    return plural


nouns = ["cat", "bus", "box", "baby", "toy", "dish"]

print("Finite-State Morphological Parser")
print("---------------------------------")

for noun in nouns:
    print(noun, "->", plural_fsm(noun))
