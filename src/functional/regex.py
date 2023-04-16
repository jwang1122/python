import re

# Create a regular expression pattern to match email addresses
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Test the pattern against a sample text
text = "Please send your inquiries to john@example.com or jane.doe@example.co.uk."
matches = re.findall(pattern, text)

# Print the matches
print(matches)

print(re.fullmatch(pattern, "jwang1122@gmail.com") is not None)
print(re.fullmatch(pattern, "jwang1122@gmail.com").string)
print(re.fullmatch(pattern, "jwang1122gmail.com"))