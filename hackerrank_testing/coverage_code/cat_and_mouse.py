import random


def randomMouseDistance():
    random_number = random.randint(1, 10)
    return random_number


def catAndMouse(x, y, z):
    z = randomMouseDistance()
    print(x, y, z)
    dx = abs(z - x)
    dy = abs(z - y)
    if dx == dy:
        return "Mouse C"
    elif dx > dy:
        return "Cat B"
    else:
        return "Cat A"
