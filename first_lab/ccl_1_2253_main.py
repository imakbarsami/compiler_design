import os

def read_and_generate(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
        
    new_file = 'ccl_1_2253_output' + ".c"

    with open(new_file, 'w') as f:
        f.write(code)

if __name__ == "__main__":
    read_and_generate("ccl_1_2253_input.c")
