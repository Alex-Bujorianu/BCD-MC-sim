#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:47:52 2021

@author: alex
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from statistics import mean, quantiles

# A simple Monte Carlo simulation representing a risk-neutral investor.
# i.e. the university will always chose to code more features

def NPV(t, i, c, d):
    "This function calculates the Net Present Value to 2 decimal places."
    list = []
    for x in range(1, t+1):
        list.append(c / (1+(d/100))**x)
    discountedvalues = sum(list)
    return round(discountedvalues - i, 2)

results = []
iterations = 20000

for i in range(1, iterations):
    #always code more features in second decision moment.
    initial_investment = np.random.gamma(15.28, 2557, 1) #mean 39,100, σ = 10,000
    discount_rate = np.random.uniform(0.0, 5.0) 
    time_period = int(np.random.gamma(25, 3/5, 1)) #gamma dist with mean = 15, σ = 3
    cashflow = 0
    event_1 = random.random()
    event_2 = random.random()
    #First possibility: adoption is wide in both decision moments
    if event_1 < 0.8 and event_2 < 0.9:
        cashflow = max(0, np.random.normal(13000, 2000))
    #Adoption is wide in the first moment but not the second
    elif event_1 < 0.8 and event_2 > 0.9:
        cashflow = max(0, np.random.normal(11000, 2000))
    #Third possibility: adoption is low in the 1st moment but high in the 2nd
    elif event_1 > 0.8 and event_2 < 0.5:
        cashflow = max(0, np.random.normal(6000, 2000))
    #Finally: adoption is low in both moments
    else:
        cashflow = max(0, np.random.normal(3000, 500))
    result = NPV(time_period, initial_investment, cashflow, discount_rate)
    results.append(result)


average = mean(results)
first_quartile = quantiles(results, n=5)[0]
print("The average is ", average, "The first quartile is ", first_quartile,
      "The lowest value is ", min(results), "the highest value is ", max(results))
lineStart = 0
lineEnd = iterations
plt.scatter(range(0, len(results), 1), results, alpha=0.8)
plt.plot([lineStart, lineEnd], [average, average], 'k-', color = 'g')
plt.plot([lineStart, lineEnd], [first_quartile, first_quartile], 'k-', color = 'r')
plt.xlabel("Simulation run number")
plt.ylabel("NPV in €")
plt.tight_layout() #Needed to avoid truncating the graph
plt.savefig("Monte-Carlo-results.png", dpi=600)