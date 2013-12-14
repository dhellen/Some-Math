#!/usr/bin/env python

# I wrote these functions in an attempt to build a combinatorics library.

from fractions import Fraction

def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)

def order_matters(n, k):
    return factorial(n) / factorial(n-k)

def any_order(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))

def prob_of_specs_given_AO(n,k,nsi):  # nsi = number of specified items
    return Fraction(anyorder(n-nsi, k-nsi), anyorder(n, k))
