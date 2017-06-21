#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Jennings Liu@ 2017-06-10 10:56:00

import numpy
temps = [31, 32, 32, 31, 28, 29, 31, 38, 32, 31, 30, 29, 30, 31, 26]
num_items = len(temps)
product = 1.
for temperature in temps:
    product *= temperature
    print('Product is %f'%product)
geometric_mean = product**(1./num_items)
print('Geometric mean of temps is %f'%geometric_mean)
