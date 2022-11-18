import unittest

from src import generator
from src import fibonacci
from src import magic_squares

# ****************************
#   fIBONACCI TESTS
# ****************************
def test_small_n_fib():
    fib_of_9 = 34
    fib_n = fibonacci.fibo(9)
    assert fib_of_9 == fib_n
    
def test_large_n_fib():
    fib_of_24 = 46368
    fib_n = fibonacci.fibo(24)
    assert fib_of_24 == fib_n

# ****************************
#   MAGIC SQUARES TESTS
# ****************************
def test_small_n_magic():
    magic_of_5 = 20.0
    magic_of_n = magic_squares.magic_square(5)
    assert magic_of_5 == magic_of_n
    
def test_large_n_magic():
    magic_of_40 = 860.0
    magic_of_n = magic_squares.magic_square(40)
    assert magic_of_40 == magic_of_n
