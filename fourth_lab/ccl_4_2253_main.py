import re

# Take regex pattern input from user
pattern = input("Enter a regular expression: ")

# Take string input to test against
test_string = input("Enter a string to match: ")

# Try matching
try:
    match = re.match(pattern, test_string)
    if match:
        print("Match found!")
        print("Matched text:", match.group())
    else:
        print("No match found.")
except re.error as e:
    print("Invalid regular expression:", e)

