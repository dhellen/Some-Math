#!/usr/bin/env python

# I wrote these functions in an attempt to write a library for
# triangular numbers.

def is_triangular(num):
    subtract = 1
    while num > 0:
        num -= subtract
        if num == 0:
            return True
        elif num > 0:
            subtract += 1
        else:
            return False

def make_tri(num):
    return sum(xrange(1,num+1))
