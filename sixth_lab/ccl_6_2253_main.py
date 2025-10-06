def detect_and_remove_left_recursion(cfg_lines):
    grammar = {}
    for line in cfg_lines:
        if "->" in line:
            left, right = map(str.strip, line.split("->"))
            grammar[left] = [p.strip() for p in right.split("|")]

    left_recursions, new_grammar = [], {}

    for nt, prods in grammar.items():
        alpha = [p[len(nt):] for p in prods if p.startswith(nt)]
        beta  = [p for p in prods if not p.startswith(nt)]

        if alpha:
            new_nt = nt + "'"
            left_recursions.extend([f"{nt} -> {nt + a}" for a in alpha])
            new_grammar[nt] = [b + new_nt for b in beta]
            new_grammar[new_nt] = [a + new_nt for a in alpha] + ["ε"]
        else:
            new_grammar[nt] = prods

    return left_recursions, new_grammar
if __name__ == "__main__":
    print("\nEnter grammar rules and Type 'enter' when finished:")
    cfg_lines = iter(input, "enter") 

    # Process grammar
    recursions, updated = detect_and_remove_left_recursion(list(cfg_lines))

    print(f"\nNo. of left recursion: {len(recursions)}")
    print("Here Left Recursion:" if recursions else "No left recursion found.")
    for r in recursions: 
        print(r)

    print("\nGrammar after removing left recursion:")
    for nt, prods in updated.items():
        print(f"{nt} -> {' | '.join(prods)}")

