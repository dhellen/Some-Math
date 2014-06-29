#!/usr/bin/env python

# Some of these functions are incomplete I guess,
# going off of the notes for the last function.
# I will come back soon and work on this, or at least decide not to.

import math

''' NOTE: Type does not matter in tests for equality; if z is a whole number,
(float(z) == int(z)) returns True.'''

''' My shrink() function divides a dividend by a divisor and then by the
quotient, and it then divides the quotient by the same divisor, and it
then it divides that new quotient, and it repeats this process for as long as
the operation continues to produce an integer quotient or once the quotient
equals 1. So...

shrink(1999, 2)  =>  125
shrink(1000, 3)  =>  1000
shrink(1000, 4)  =>  250
shrink(1000, 10)  =>  1
'''
def shrink(z, y):
    while float(z)/y == int(z/y): z /= y
    return z

''' This function tests for whether the list passed to it only contains primes
after the first element. Should not be used on its own unless you only want to
know if alist[1:] are all primes. In other words, I wrote for use in other
functions.'''
def only_dividend_and_primes(alist):
    return True if False not in map(test_for_prime, alist[1:]) else False

def test_for_prime(z):
    if z == 1:
        return False
    for i in xrange(2, int(math.sqrt(z)+1)):
        if z % i == 0:
            return False
    return True

def is_a_num_and_its_prime_factors(alist):
    if only_dividend_and_primes(alist) and has_all_prime_factors(alist):
        return True
    else:
        return False

# Work this last function into other functions in this script to improve them
def all_are_factors_of_first(alist): 
    for i in alist[1:]:
        if alist[0] % i != 0:
            return False
    return True
