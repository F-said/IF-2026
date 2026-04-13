import module2

print(module2.GREETING)
print(module2.LANGUAGE)

print(module2.greet("Alice"))
print(module2.shout("python"))

students = ["Alice", "Bob", "Carlos"]
messages = module2.greet_all(students)
for message in messages:
    print(message)

words = ["cat", "python", "dog", "programming", "loop"]
long_words = module2.collect_long_words(words)
print(long_words)
