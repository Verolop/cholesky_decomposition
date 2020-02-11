#!/usr/bin/env python
# -*- coding: utf-8 -*-
#whatever lol
from math import sqrt
from pprint import pprint

def cholesky(A):    
    n = len(A)
    
    L = [[0.0] * n for i in xrange(n)]
    
    for i in xrange(n):
        for k in xrange(i+1):
            suma = sum(L[i][j]* L[k][j] for j in xrange(k))

            if (i==k):
                L[i][k] = sqrt(A[i][i] - suma)
            else:
                L[i][k] = (1.0 / L[k][k]* (A[i][k] - suma))

    return L 

#Sample symmetric, postive matrix
A= [[1, 3, 5], [3, 13, 23], [5, 23, 42]]
L = cholesky(A)

print "A= "
pprint(A)

print "L="
pprint(L)

