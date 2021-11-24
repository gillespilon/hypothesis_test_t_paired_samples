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
"""

from pathlib import Path
import time

import datasense as ds
import pandas as pd


def main():
    pass


if __name__ == "__main__":
    main()
