#!/usr/bin/env python

# I got really excited about the recursive functions that come with Python

# Factorial
def factorial(z):
    return reduce((lambda a, b: a*b), xrange(1, z+1))

# Some narrow functions as reference for broader functions:

''' A. The sum of squares is limited to only getting sums with exponent of 2,
so here is a function to calculate the sum (or series, really) of a power of
your choosing:'''
def series_of_powers(z, expo):
    return sum([y**expo for y in xrange(1, z+1)])

# B. Square of power of sums (or series, really):
def series_to_a_power(z, expo):
    return (sum(xrange(1, z+1)))**expo

''' I heard you liked functions, so I put a bunch of function parameters in
these function parameters, so you can pass functions to your functions.
'''

''' Operation of powers (think sum of squares, but it's any operation and any
exponent). I made xrange go backwards so that lambdas for subtracting and
dividing would make sense.
'''
def oppower(z, expo, alambdaorfunc):
    return reduce(alambdaorfunc, [y**expo for y in xrange(z, 0, -1)])

''' For example:
oppower(6,2,lambda z,y: z-y)
produces 6**2 - 5**2 - 4**2 - 3**2 - 2**2 - 1**2, or -19
'''

''' Power of operations (think square of sums). Again, I made xrange go
backwards so that lambdas for subtracting and dividing would make sense.
'''
def powops(z, expo, alambdaorfunc):
    return (reduce(alambdaorfunc, xrange(z, 0, -1)))**expo

''' For example
powops(6,3,lambda z,y:z**y)
carries out ( (((((6**5)**4)**3)**2)**1) )**3, which is:
13628565259765240063307214694325589634102920113198019054884331531100689326724922
71228635903677560908387368131503998319547415800033207941032383559081748787333663
34155884618443998783841969103173072216240445102125485099344220416740519344692695
59871047548851882918239704585019039154176L
'''

''' It occurred to me as I was recording the example for powops() that factorial
is a bit limited. So, here is another function based on factorial that you can
customize. It differs from simply just a call to reduce(<function>, <sequence>)
because I set an xrange that goes backwards as the sequence for every call.
'''
def hacktorial(z, alambdaorfunc):
    return reduce(alambdaorfunc, xrange(z, 0, -1))
