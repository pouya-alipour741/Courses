def add(x, y):
    return x + y


def divide(x, y):
    if y == 0:
        raise ValueError('can\'t divide by 0')
    return x / y