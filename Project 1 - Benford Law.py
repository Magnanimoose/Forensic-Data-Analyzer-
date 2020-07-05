"""Project 1: Benford's Law"""
from math import log10
from math import trunc
import numpy as np
import random
from scipy.stats import ks_2samp


from tkinter import *

# This is my first ever attempt at making an app on Python,


float_list = random.randrange((1, 300, 1))
print(str(float_list) + 'Test')

# [11, 2.35, 27.0, 654, 2678, 83, 133, 5233, 43, 785, 34, 12069, ]


'''1.0 DATA CHECK: is the data eligible for Benford? First check if all data is float, then if has good scale of 
magnitude then check if has enough elements'''


def data_check(list):
    truth_array = [] # Bool array to check which steps the data passed curation
    if all(isinstance(float(i), float) for i in list):  # This converts all int to float then checks if all i are float
        truth_array += 'T'
    else:
        truth_array += 'F'
    if len(list) >= 4:  # Checks if array has the desired cardinal
        truth_array += 'T'
    else:
        truth_array += 'F'
    if max(abs(i) >=100 for i in list):  # Checks the order of magnitude
        truth_array += 'T'
    else:
        truth_array += 'F'
    if truth_array == ['T', 'T', 'T']:
        return first_digit(list)
    else:
        print(truth_array)


'''2.0 Retrieve first digit function'''


def first_digit(list):
    first_dig = []
    for n in list:
        while n >= 10:
            n = n / 10
        if n <= 10:
            first_dig.append(trunc(n))  # This line always rounds down

    # print(str(first_dig) + ' this is a list of only the first digits')
    return first_dig


'''2.1 Count frequency of first digits '''


def count_digit(list):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    for i in list:
        if i is 1:
            count1 += 1
        elif i is 2:
            count2 += 1
        elif i is 3:
            count3 += 1
        elif i is 4:
            count4 += 1
        elif i is 5:
            count5 += 1
        elif i is 6:
            count6 += 1
        elif i is 7:
            count7 += 1
        elif i is 8:
            count8 += 1
        elif i is 9:
            count9 += 1
    t_count = [count1, count2, count3, count4, count5, count6, count7, count8, count9]
    x = sum(t_count)
    first_digit_freq = [count1/x, count2/x, count3/x, count4/x, count5/x, count6/x, count7/x, count8/x, count9/x]
    #print(first_digit_freq)
    return first_digit_freq


"""3.0 Benford's Law """
# This function generates the frequency of each first digits


def benford_law():
    ben_freq = []
    for i in range(1, 10):
        x = log10(1+1/i)
        ben_freq.append(x)
    return ben_freq


#y = count_digit(data_check(float_list))
y1 = np.array((y))
bl = benford_law()
b2 = np.array((bl))


# headings = ['First digit', 'Benford freq', 'Data freq']
# digits = array((1, 2, 3, 4, 5, 6, 7, 8, 9))
# result_table = column_stack((digits, bl, y1))
# print(headings)
# print(result_table)

'''4.0  Kolmogorov-Smirnov'''

#ks = ks_2samp(y1, b2)
#print(ks)
#https://stackoverflow.com/questions/37424877/typeerrorndarray-not-callable-in-scipy-stats-kstest
#https://docs.scipy.org/doc/scipy-0.7.x/reference/generated/scipy.stats.kstest.html

# # Now I need to create a comparison function, plot a graph with 2 lines and investigate chi square to curate data.
# Use Tkinter to create a GUI, pandas to accept Excel files,
# Create a interactive user quiz to ask them questions about their data
# inc citations
# Input random list of data
# Learn how to interpret KS test
# Plot graphs
