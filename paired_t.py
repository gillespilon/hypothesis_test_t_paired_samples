#! /usr/bin/env python3
"""
“Paired” means that there is a one-to-one correspondence between the values in
two samples. If  𝑥1,𝑥2,...,𝑥𝑛  and  𝑦1,𝑦2,...,𝑌𝑛  are two samples, then 𝑥𝑖
corresponds to  𝑦𝑖 .

Example. A sample of a product is taken from a process. Measurements are made
of the “before” condition. The products are potentially changed in some way,
such as a cleaning step. The “before” and “after” measurements of a
characteristic are made with the same device, on the same  𝑛  units. Each
“before” measurement is paired with the corresponding “after” measurement and
the differences are calculated.

A paired t test can be used for:

Is the average of the differences not equal to zero?
Is the average of the differences greater than zero?
Is the average of the differences less than zero?
Is the average of the differences not equal to some hypothesized average?
Is the average of the differences greater than some hypothesized average?
Is the average of the differences less than some hypothesized average?

For t tests in general:

The data in a sample follow a normal distribution mean  𝜇  and variance  𝜎2 .
The sample variance  𝑠2  follows a  𝜒2  distribution with  𝜌  degrees of
freedom under the null hypothesis, where  𝜌  is a positive constant.
(𝑌⎯⎯⎯⎯−𝜇)  and the sample standard deviations  𝑠  are independent.
"""

from pathlib import Path
import time

import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats
import datasense as ds
import pandas as pd
import numpy as np



def main():
    hypothesized_difference = 4
    significance_level = 0.05
    df = pd.read_csv('data_paired_t.csv')
    df_before_after = df[['before', 'after']]
    difference_calc = df['after'] - df['before']


if __name__ == "__main__":
    main()
