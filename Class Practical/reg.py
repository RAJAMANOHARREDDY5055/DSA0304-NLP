
import re

text = "My name is Raja and my number is 9876543210"

# Match a pattern at the beginning
print(re.match("My", text).group())

# Search for a pattern anywhere
print(re.search("Raja", text).group())

# Find all numbers in the text
print(re.findall(r"\d+", text))
