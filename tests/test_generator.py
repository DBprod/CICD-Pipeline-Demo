import unittest

from src import generator


def test_small_n():
    fib_of_9 = 34
    fib_n = generator.fibo(9)
    assert fib_of_9 == fib_n
    

def test_large_n():
    fib_of_24 = 46368
    fib_n = generator.fibo(24)
    assert fib_of_24 == fib_n