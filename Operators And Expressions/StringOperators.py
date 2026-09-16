# String Concatenation (+)

first_name = "Sajan"
last_name = "Thakuri"
full_name = first_name + " " + last_name
print(full_name)


# String Repetition (*)
word = "Hello "
repeat_count = 3
repeated_word = word * repeat_count
print(repeated_word)


# String Comparison or Relational Operators (==, !=, <, >, <=, >=)
name1 = "Sajan"
name2 = "Sajan"
name3 = "John"

print(name1 == name2)  # True
print(name1 == name3)  # False
print(name1 != name3)  # True
print(name1 < name3)  # True (lexicographically)
print(name1 > name3)  # False (lexicographically)


# String Membership Operators (in, not in)
sentence = "Python is a powerful programming language."
print("Python" in sentence)  # True
print("Java" not in sentence)  # True


# String Slicing and Indexing
text = "Hello, World!"
print(text[0])  # H (first character)
print(text[-1])  # ! (last character)
print(text[0:5])  # Hello (substring from index 0 to 4)
print(text[7:])  # World! (substring from index 7 to the end)
print(text[:5])  # Hello (substring from the start to index 4)
