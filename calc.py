# content of test_sample.py
def func(x):
    return x + 1
def func2(x):
    return x + 2

def test_answer():
    assert func(2) == 3

def test_answer2():
    assert func2(2) == 4