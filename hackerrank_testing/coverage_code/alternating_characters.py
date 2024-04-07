import random
import string


def random_string():
    characters = string.ascii_letters
    length = random.randint(1, 20)
    random_string = "".join(random.choice(characters) for _ in range(length))
    return random_string

def alternatingCharacters(s):
    s = random_string()
    delete = 0
    for i in range(len(s)-1) :
        if s[i] == s[i+1] :
            delete += 1
    return delete

print(random_string())