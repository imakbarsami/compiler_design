from collections import defaultdict
def parse_grammar():
    grammar = {}
    order = []  
    print("Enter grammar productions : ")
    print("Type 'end' to finish.")

    while True:
        line = input().strip()
        if line.lower() == "end":
            break
        if "->" not in line:
            print("Invalid format! Use: A -> ab | ac | d")
            continue

        lhs, rhs = line.split("->")
        lhs = lhs.strip()
        rhs = rhs.strip().split("|")
        grammar[lhs] = [list(prod.strip()) for prod in rhs]
        order.append(lhs)

    return grammar, order


def detect_left_factoring(grammar):
    left_factors = {}
    count = 0

    for non_terminal, productions in grammar.items():
        prefix_dict = defaultdict(list)
        for prod in productions:
            if prod:
                prefix_dict[prod[0]].append(prod)

        for prefix, group in prefix_dict.items():
            if len(group) > 1:  
                count += 1
                if non_terminal not in left_factors:
                    left_factors[non_terminal] = []
                left_factors[non_terminal].append(group)

    # Print result
    if count == 0:
        print("\nNo left factoring detected.")
    else:
        print(f"\nTotal {count} left factoring(s) detected:")
        for nt, groups in left_factors.items():
            for g in groups:
                print(f"{nt} → {[''.join(p) for p in g]}")

    return left_factors


def remove_left_factoring(grammar):
    new_grammar = {}
    primes = defaultdict(int)

    for non_terminal, productions in grammar.items():
        prefix_dict = defaultdict(list)
        for prod in productions:
            if prod:
                prefix_dict[prod[0]].append(prod)

        new_productions = []
        extra_rules = {}

        for prefix, group in prefix_dict.items():
            if len(group) > 1:  
                primes[non_terminal] += 1
                new_nt = non_terminal + "'" * primes[non_terminal]
                new_productions.append([prefix, new_nt])
                remainder = []
                for g in group:
                    remainder.append(g[1:] if len(g) > 1 else ["ε"])
                extra_rules[new_nt] = remainder
            else:
                new_productions.append(group[0])

        new_grammar[non_terminal] = new_productions
        for k, v in extra_rules.items():
            new_grammar[k] = v  

    return new_grammar



if __name__ == "__main__":
    grammar, order = parse_grammar()
    detect_left_factoring(grammar)
    factored_grammar = remove_left_factoring(grammar)

    print("\nGrammar After Left Factoring:")
    for nt in order:
        if nt in factored_grammar:
            print(f"{nt} → {' | '.join(''.join(p) for p in factored_grammar[nt])}")
            for k in factored_grammar.keys():
                if k.startswith(nt + "'"):
                    print(f"{k} → {' | '.join(''.join(p) for p in factored_grammar[k])}")
