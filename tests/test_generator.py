import unittest


from src import fibonacci
from src import magic_squares
from src import lazyCarter
from src import magic_squares
from src import primeNumbers

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

# ****************************
#   LAZY CARTER TESTS
# ****************************
def test_10_n_lazy():
    lazy_of_10 = 230
    lazy_n = lazyCarter.lazyCarterSum(10)
    assert lazy_of_10 == lazy_n

def test_4_n_lazy():
    lazy_of_3 = 13
    lazy_n = lazyCarter.lazyCarterSum(3)
    assert lazy_of_3 == lazy_n

# ****************************
#   MAGIC SQUARE TESTS
# ****************************
def test_49_n_square():
    sum_square_of_49 = 1274
    sum_square_n = magic_squares.magic_square(49)
    assert sum_square_of_49 == sum_square_n

def test_20_n_square():
    sum_square_of_20 = 230
    sum_square_n = magic_squares.magic_square(20)
    assert sum_square_of_20 == sum_square_n

# ****************************
#   PRIME NUMBER TESTS
# ****************************
def test_30_n_PRIME():
    sum_prime_of_30 = 129
    sum_square_n = primeNumbers.sumOfPrimes(30)
    assert sum_prime_of_30 == sum_square_n

def test_49_n_PRIME():
    sum_prime_of_49 = 328
    sum_prime_n = primeNumbers.sumOfPrimes(49)
    assert sum_prime_of_49 == sum_prime_n