import re

def remove_comments_and_analyze(filename_in, filename_out):
    with open(filename_in, 'r') as file:
        code = file.read()

    # Patterns
    single_line_pattern = r'//.*'
    multi_line_pattern = r'/\*[\s\S]*?\*/'

    # Find all comments
    single_line_comments = re.findall(single_line_pattern, code)
    multi_line_comments = re.findall(multi_line_pattern, code)

    # Stats
    has_single = "yes" if single_line_comments else "no"
    has_multi = "yes" if multi_line_comments else "no"
    count_single = len(single_line_comments)
    count_multi = len(multi_line_comments)

    # Display results
    print(f"Single line comment Exist: {has_single}")
    print(f"Multi line comment Exist: {has_multi}")
    print(f"Single line comment : {count_single}")
    print(f"Multi line comment : {count_multi}")

    # Remove comments
    code_no_comments = re.sub(multi_line_pattern, '', code)
    code_no_comments = re.sub(single_line_pattern, '', code_no_comments)

    # Write output to new file
    with open(filename_out, 'w') as out_file:
        out_file.write(code_no_comments)

# Usage
input_file = 'ccl_2_2253_input.c'
output_file = 'ccl_2_2253_output.c'
remove_comments_and_analyze(input_file, output_file)
