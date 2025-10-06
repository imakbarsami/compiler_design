import re
from collections import Counter

# set of keywords
c_keywords = {
    'break','case','char','const','continue','default',
    'do','double','else','float','for','if','int','long','return',
    'struct','switch','union','void','while','include'
}

#read input file
with open('ccl_3_2253_input.c', 'r') as f:
    original_code = f.read()

#remove comments
no_comments = re.sub(r'//.*', '', original_code)
no_comments = re.sub(r'/\*.*?\*/', '', no_comments, flags=re.DOTALL)

# save the output file
with open('ccl_3_2253_output.c', 'w') as f:
    f.write(no_comments)

#extract string contents
string_literals = re.findall(r'"(.*?)"', no_comments)

#combine string contents
all_strings = ' '.join(string_literals)

# tokenize and filter string keywords
string_keywords = [word for word in re.findall(r'\b\w+\b', all_strings) if word in c_keywords]

#remove string from the code for keyword analysis
code_no_strings = re.sub(r'"(\\.|[^"\\])*"', '', no_comments)

#tokenize and count keywords ---
tokens = re.findall(r'\b\w+\b', code_no_strings)
keyword_counts = Counter(token for token in tokens if token in c_keywords)

#displaying results
print(f"\nTotal Unique Keywords: {len(keyword_counts)}")
for kw, count in keyword_counts.items():
    print(f"{kw}: {count}")

# displaying keywords inside string literals
if string_keywords:
    print("displaying :", ' '.join(string_keywords))


