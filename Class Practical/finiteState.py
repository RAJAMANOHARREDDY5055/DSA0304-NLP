# Finite State Automaton to recognize strings ending with 'ab'

def finite_automaton(string):
    state = 'q0'

    for char in string:
        if state == 'q0':
            if char == 'a':
                state = 'q1'
            else:
                state = 'q0'

        elif state == 'q1':
            if char == 'a':
                state = 'q1'
            elif char == 'b':
                state = 'q2'
            else:
                state = 'q0'

        elif state == 'q2':
            if char == 'a':
                state = 'q1'
            else:
                state = 'q0'

    # q2 is the accepting state
    return state == 'q2'


# Test the automaton
strings = ["ab", "ac","aab", "cab", "abc", "aba", "abb"]

for string in strings:
    if finite_automaton(string):
        print(string, "-> Accepted")
    else:
        print(string, "-> Rejected")