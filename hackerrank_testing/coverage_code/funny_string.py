import random
import string


def random_string():
    characters = string.ascii_lowercase
    random_string = "".join(random.choice(characters) for _ in range(10))
    return random_string


def funnyString(s):
    s = random_string()
    r = s[::-1]
    for i in range(len(s) - 1):
        a = abs(ord(s[i]) - ord(s[i + 1]))
        b = abs(ord(r[i]) - ord(r[i + 1]))
        if a != b:
            return "Not Funny"
    return "Funny"

print(random_string())
