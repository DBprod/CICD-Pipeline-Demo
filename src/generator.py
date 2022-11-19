from src import fibonacci 
from src import magic_squares 
from src import lazyCarter
from src import primeNumbers
from src import squareSeries
import random as r


def generate_random_series(n):
    # Initialize a list of the series
    # index's 0 = fibo, 1 = magic, 2 = prime, 3= lazy, 4 =square_num 
    # select randomly which function to display
    rand_series =  r.randint(0,4)
    return generate_title_sum(rand_series, n)


def generate_title_sum(rand_series, n):
    t = ''
    sum = 0
    if rand_series == 0:
        t = 'Fibonacci Sum is:'
        sum = fibonacci.fibo(n)
    elif rand_series == 1:
        t = 'Sum of Magic Square Series is:'
        sum = magic_squares.magic_square(n)
    elif rand_series == 2:
        t = 'Sum of Prime Number Sequence is:'
        sum = primeNumbers.sumOfPrimes(n)
    elif rand_series == 3:
        t = "Sum of Lazy Caterer's Sequence is:"
        sum = lazyCarter.lazyCarterSum(n)
    else:
        t = 'Sum of Square Numbers Series is:'
        sum = squareSeries.squareSeries(n)
    
    return sum, t