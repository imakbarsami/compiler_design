from collections import defaultdict

def parse_grammar():
    print("Enter grammar productions. Type 'done' when finished:")

    lines = []
    while True:
        line = input().strip()
        if line.lower() == "done":
            break
        if line:
            lines.append(line)

    grammar = defaultdict(list)
    nonterminals = []

    # Collect nonterminals (LHS)
    for line in lines:
        lhs = line.split("->")[0].strip()
        nonterminals.append(lhs)
    nonterminals_sorted = sorted(nonterminals, key=len, reverse=True)

    def tokenize(prod_str):
        tokens = []
        s = prod_str.strip()
        i = 0
        while i < len(s):
            if s[i].isspace():
                i += 1
                continue
            matched = False
            # Match full nonterminal names first
            for nt in nonterminals_sorted:
                if s.startswith(nt, i):
                    tokens.append(nt)
                    i += len(nt)
                    matched = True
                    break
            if matched:
                continue
            # Lowercase = terminal (multi-char like 'id')
            if s[i].islower():
                j = i
                while j < len(s) and s[j].islower():
                    j += 1
                tokens.append(s[i:j])
                i = j
            # Uppercase = nonterminal (with possible prime ')
            elif s[i].isupper():
                j = i + 1
                while j < len(s) and (s[j].isupper() or s[j] == "'"):
                    j += 1
                tokens.append(s[i:j])
                i = j
            else:
                tokens.append(s[i])
                i += 1
        return tokens

    # Build grammar dict
    for line in lines:
        lhs, rhs = line.split("->", 1)
        lhs = lhs.strip()
        for alt in rhs.split("|"):
            alt = alt.strip()
            if alt in ["ε", "e", "eps"]:
                grammar[lhs].append(["ε"])
            else:
                grammar[lhs].append(tokenize(alt))
    return dict(grammar)

def firstSet(grammar):
    nonterminals = set(grammar.keys())
    rhs_symbols = {sym for prods in grammar.values() for prod in prods for sym in prod}
    terminals = {s for s in rhs_symbols if s not in nonterminals and s != "ε"}

    FIRST = {sym: set() for sym in nonterminals.union(terminals)}
    for t in terminals:
        FIRST[t].add(t)

    changed = True
    while changed:
        changed = False
        for A in nonterminals:
            for prod in grammar[A]:
                if prod == ["ε"]:
                    if "ε" not in FIRST[A]:
                        FIRST[A].add("ε")
                        changed = True
                    continue
                add_epsilon = True
                for sym in prod:
                    if sym in terminals:
                        if sym not in FIRST[A]:
                            FIRST[A].add(sym)
                            changed = True
                        add_epsilon = False
                        break
                    before = len(FIRST[A])
                    FIRST[A].update(FIRST[sym] - {"ε"})
                    if len(FIRST[A]) != before:
                        changed = True
                    if "ε" in FIRST[sym]:
                        add_epsilon = True
                        continue
                    else:
                        add_epsilon = False
                        break
                if add_epsilon:
                    if "ε" not in FIRST[A]:
                        FIRST[A].add("ε")
                        changed = True
    return FIRST, nonterminals, terminals

def format_set(s):
    items = sorted([x for x in s if x != "ε"])
    if "ε" in s:
        items.append("ε")
    return "{" + ",".join(items) + "}"

def print_firsts(FIRST, nonterminals, terminals):
    print("\nFor Terminal:")
    for t in sorted(terminals):
        print(f"First({t})={format_set(FIRST[t])}")
    print("\nFor Non Terminal:")
    for nt in sorted(nonterminals):
        print(f"First({nt})={format_set(FIRST[nt])}")

if __name__ == "__main__":
    grammar = parse_grammar()
    FIRST, nonterminals, terminals = firstSet(grammar)
    print_firsts(FIRST, nonterminals, terminals)
