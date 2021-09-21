from importlib.resources import read_text


def greet():
    greeting = read_text('walrus.data', 'greeting.txt')
    return greeting
