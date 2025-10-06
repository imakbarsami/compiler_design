def detect_left_recursion(cfg_lines):
    grammar = {}
    for line in cfg_lines:
        if "->" in line:
            left, right = map(str.strip, line.split("->"))
            grammar[left] = [p.strip() for p in right.split("|")]

    left_recursions = []

    for nt, prods in grammar.items():
        for p in prods:
            if p.startswith(nt):   # left recursion detect
                left_recursions.append(f"{nt} -> {p}")

    return left_recursions


if __name__ == "__main__":
    print("\nEnter grammar rules and Type 'enter' when finished:")
    cfg_lines = iter(input, "enter") 

    # Process grammar
    recursions = detect_left_recursion(list(cfg_lines))

    print(f"\nNo. of left recursion: {len(recursions)}")
    print("Here Left Recursion:" if recursions else "No left recursion found.")
    for r in recursions: 
        print(r)
