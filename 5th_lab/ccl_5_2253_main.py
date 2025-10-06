import re

def remove_comments(code):
    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    return code

def remove_strings(code):
    return re.sub(r'"(\\.|[^"\\])*"', '', code)

def extract_identifiers(code):
    identifiers = {}

    # header files
    includes = re.findall(r'#include<([a-zA-Z_]\w*)\.h>', code)
    for inc in includes:
        identifiers[inc] = identifiers.get(inc, 0) + 1

    # remove after . 
    code_wo_includes = re.sub(r'#include<[^>]+>', '', code)
    # all variable and function names
    tokens = re.findall(r'\b[_a-zA-Z]\w*\b', code_wo_includes)
    keywords = {
        'int', 'float', 'char', 'double', 'long', 'short', 'void', 'return',
        'if', 'else', 'for', 'while', 'do', 'switch', 'case', 'break', 'continue',
        'struct', 'union', 'enum', 'typedef', 'sizeof', 'main',
        'include'
    }
    for token in tokens:
        if token not in keywords:
            identifiers[token] = identifiers.get(token, 0) + 1

    return identifiers
def main():
    input_filename = 'ccl_5_2253_input.c'
    output_filename = 'ccl_5_2253_output.c'

    with open(input_filename, 'r') as file:
        code = file.read()
    code_no_comments = remove_comments(code)
    code_no_strings = remove_strings(code_no_comments)
    #extract identifiers
    identifier_counts = extract_identifiers(code_no_strings)
    # print counts
    print("output:")
    for key, count in sorted(identifier_counts.items()):
        print(f"\t{key} = {count}")

    with open(output_filename, 'w') as out_file:
        out_file.write(code_no_comments)
main()


