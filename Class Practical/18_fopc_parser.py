
import re

TOKEN = re.compile(r"\\s*(<->|->|AND\\b|OR\\b|NOT\\b|FORALL\\b|EXISTS\\b|[A-Za-z_]\\w*|[(),.]|\\S)", re.I)

def tokenize(text):
    return [m.group(1) for m in TOKEN.finditer(text)]

def parse_atom(tokens, i):
    if i >= len(tokens) or not re.fullmatch(r"[A-Za-z_]\\w*", tokens[i]):
        raise ValueError("Expected predicate or identifier")
    name = tokens[i]
    i += 1
    if i < len(tokens) and tokens[i] == "(":
        i += 1
        args = []
        while i < len(tokens) and tokens[i] != ")":
            if not re.fullmatch(r"[A-Za-z_]\\w*", tokens[i]):
                raise ValueError("Expected argument")
            args.append(tokens[i]); i += 1
            if i < len(tokens) and tokens[i] == ",":
                i += 1
            elif i < len(tokens) and tokens[i] != ")":
                raise ValueError("Expected ',' or ')'")
        if i >= len(tokens) or tokens[i] != ")":
            raise ValueError("Missing ')'")
        return (name, args), i + 1
    return (name, []), i

def parse_expression(tokens):
    if not tokens:
        raise ValueError("Empty expression")
    i = 0
    prefix = None
    if tokens[i].upper() in {"NOT", "FORALL", "EXISTS"}:
        prefix = tokens[i].upper(); i += 1
        if prefix in {"FORALL", "EXISTS"}:
            if i >= len(tokens) or not re.fullmatch(r"[A-Za-z_]\\w*", tokens[i]):
                raise ValueError("Quantifier must be followed by a variable")
            variable = tokens[i]; i += 1
            if i < len(tokens) and tokens[i] == ".":
                i += 1
            atom, i = parse_atom(tokens, i)
            node = (prefix, variable, atom)
        else:
            atom, i = parse_atom(tokens, i)
            node = (prefix, atom)
    else:
        node, i = parse_atom(tokens, i)
    while i < len(tokens):
        op = tokens[i].upper()
        if op not in {"AND", "OR", "->", "<->"}:
            raise ValueError(f"Unexpected token: {tokens[i]}")
        i += 1
        right, i = parse_atom(tokens, i)
        node = (op, node, right)
    return node

expression = input("Enter FOPC expression (example: Loves(John, Mary)): ").strip()
try:
    tokens = tokenize(expression)
    tree = parse_expression(tokens)
    print("Valid in this simple FOPC subset.")
    print("Parsed structure:", tree)
except ValueError as error:
    print("Invalid expression:", error)
