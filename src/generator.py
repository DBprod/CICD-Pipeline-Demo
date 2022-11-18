from __future__ import print_function
from src import fibonacci as fibo
from src import magic_squares as magic
import random as r


def generate_random_series(n):
    # Initialize a list of the series
    # index's 0 = fibo, 1 = magic, 2 = look_say, 3= lazy, 4 =square_num 
    # select randomly which function to display
    rand_series =  r.randint(0,4)
    return generate_title_sum(rand_series, n)


def generate_title_sum(rand_series, n):
    t = ''
    sum = 0
    if rand_series == 0:
        t = 'Fibonacci Sum is:'
        sum = fibo.fibo(n)
    elif rand_series == 1:
        t = 'Sum of Magic Square Series is:'
        sum = magic.magic_square(n)
    elif rand_series == 2:
        t = 'Sum of Look and Say Sequence is:'
        sum = fibo.fibo(n)
    elif rand_series == 3:
        t = "Sum of Lazy Caterer's Sequence is:"
        sum = fibo.fibo(n)
    elif rand_series == 4:
        t = 'Sum of Square Numbers Series is:'
        sum = fibo.fibo(n)
    
    return sum, t