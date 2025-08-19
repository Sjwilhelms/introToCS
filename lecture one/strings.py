text = "hello world"
name = "    John McGarnangle    "
sentence = "Python is Awesome"

# case methods
text.lower()
text.upper()
text.title()
text.capitalize()

# whitespace methods
name.strip()
name.lstrip()
name.rstrip()

# finding and checking
text.find("world")
text.count("l")
text.startswith("hello")
text.endswith("world")

# booleans
"123".isdigit()
"abc".isalpha()

# splitting and joining

words = sentence.split()
sentence.split("is")

" ".join(words)
"-".join(words)

# string replacement

message = "I love Java Programming"
message.replace("Java", "Python")
message.replace("0", "O", 1)
