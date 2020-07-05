"""Project 1: Benford's Law"""
from math import log10
from math import trunc
import numpy as np
import random
from scipy.stats import kstest
from tkinter import *
from sys import exit  # This command halts run

# This is my first ever attempt at making an app on Python,
#float_list = random.randrange((1, 300, 1))
#print(str(float_list) + 'Test')

list1 = ['Tom', 11, '2', 27.5, 430, 923, 7465, 4, 873, "2T"]


'''1.0 DATA Curation: is the data eligible for a Benford distribution comparison? Check if the data has a
significant enough size then if it has a big enough magnitude'''


def string_value_filter(list):
    # This function filters down to numerical values regardless if str or int
    digit_list = []
    for i in list:
        try: int(i), digit_list.append(int(i))
        except ValueError:
            pass
    return digit_list

s
def data_check(list):
    truth_array = [] # Bool array to check which steps the data passed curation
    if len(list) >= 4:  # Checks if array has the desired cardinal
        truth_array += 'T'
    else:
        truth_array += 'F'
    if max(abs(i) >=100 for i in list):  # Checks the order of magnitude
        truth_array += 'T'
    if truth_array == ['T', 'T']:
        return count_digit(list)
    else:
        return print("Data is not valid for Benford test"), exit()


'''2.0 Retrieve first digit values from data and put it into a cumulative frequency function'''


def count_digit(list):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in list:
        i = str(i)
        if i.isalpha():
            pass
        elif i.isdigit():
            digit1 = i[0]
            digit1 = int(digit1)
            count[digit1 - 1] += 1
        elif float(i):
            digit1 = i[0]
            digit1 = int(digit1)
            count[digit1 - 1] += 1
    x = sum(count)
    d_freq = [c/x for c in count]
    print(str(count) + " - This is the num of times 1-9 appeared as first digit.")
    print(d_freq)
    return d_freq


"""3.0 Benford's Law """
# This function generates the Benford frequency of each first digit

benford_freq = [log10(1 + 1/x) for x in range(1, 10)]
print(str(benford_freq) + ' This is the Benford dist array)')
for i in range(len(benford_freq)):
    ba = (benford_freq[i])


'''4.0 Table of Results'''

y = data_check(string_value_filter(list1))
y1 = np.array((y))
bl = benford_freq
b2 = np.array((bl))
headings = ['First digit', 'Benford freq', 'Data freq']
digits = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9))
result_table = np.column_stack((digits, bl, y1))
print(headings)
print(result_table)

'''5.0  Kolmogorov-Smirnov'''

ks = kstest(y1, ba)
print(ks)
#https://stackoverflow.com/questions/37424877/typeerrorndarray-not-callable-in-scipy-stats-kstest
#https://docs.scipy.org/doc/scipy-0.7.x/reference/generated/scipy.stats.kstest.html

"""MAIN FUNCTION"""

# It appears that mathematically the one sample ks test cannot be used because the Benford dist doesnt have the
# CDF property i.e. F(X) = P(x < X)

# Makes sure data check accepts floats, and string values that r floats
# # Now I need to create a comparison function, plot a graph with 2 lines and investigate chi square to curate data.
# Use Tkinter to create a GUI, pandas to accept Excel files,
# Create a interactive user quiz to ask them questions about their data
# inc citations
# Input random list of data
# Learn how to interpret KS test
# Plot graphs
# include main function

