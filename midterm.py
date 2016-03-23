#! /usr/bin/env python

"""
File: midterm.py
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: Midterm
Date: March 22, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Midterm
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def sequence(x0, r, N = 100):
    if (r < 2.9 or r > 4.0):
        print "This function is defined only where r is a real value in [2.9, 4]. Please supply an r value in the range."
    elif (x0 < 0 or x0 > 1):
        print "This function is defined only where x0 is a real value in the range [0, 1]. Please supply an x0 value in the range."
    else:
        x = [x0]
        for i in xrange(N):
            x.append(r * x[i] * (1 - x[i]))
        return x

def graph(x0, r, N = 100):
    fig = plt.figure(1)
    x = np.linspace(0, N, N + 1)
    y = sequence(x0, r, N)
    plt.plot(x, y, 'b-')
    plt.xlabel('n')
    plt.ylabel('xn')
    plt.title('sequence(n)')
    plt.show()

def asymptote_graph(x0, r1, r2, mesh, N):
    number_points = (r2 - r1) / mesh
    rspace = np.linspace(r1, r2, number_points + 1)
    y = [sequence(x0, elem, N)[-101:-1] for elem in rspace]
    fig = plt.figure(1)
    plt.plot(rspace, [elem for elem in y], 'b-')
    plt.xlabel('r')
    plt.ylabel('xn')
    plt.title('xn vs. r')
    plt.show()

def zoom_graph(x0, r1, r2, mesh, N, axis):
    number_points = (r2 - r1) / mesh
    rspace = np.linspace(r1, r2, number_points + 1)
    y = [sequence(x0, elem, N)[-101:-1] for elem in rspace]
    fig = plt.figure(1)
    plt.plot(rspace, [elem for elem in y], 'b-')
    plt.axis([axis[0], axis[1], axis[2], axis[3]])
    plt.xlabel('r')
    plt.ylabel('xn')
    plt.title('xn vs. r')
    plt.show()

def test_sequence():
    assert (sequence(0.5, 3.2, 5)[2] == 0.512), "Failure"