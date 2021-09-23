from walrus.greet import greet


def test_greeting():
    assert greet() == 'Hello World\n' 
