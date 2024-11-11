# Creating a string
text = "Hello, World!"

# Accessing characters
print(text[7])  # Output: W

# String methods
print(text.lower())       # Output: hello, world!
print(text.replace("World", "Python"))  # Output: Hello, Python!

# Splitting and joining
words = text.split(", ")
print(words)  # Output: ['Hello', 'World!']
joined_text = " - ".join(words)
print(joined_text)  # Output: Hello - World!
