GREETING = "Hello"
LANGUAGE = "Python"


def greet(name):
    return GREETING + ", " + name + "!"


def shout(word):
    return word.upper()


def greet_all(names):
    messages = []
    for name in names:
        greeting = greet(name)
        messages.append(greeting)
    return messages


def collect_long_words(words):
    long_words = []
    for word in words:
        if len(word) > 4:
            long_words.append(word)
    return long_words
