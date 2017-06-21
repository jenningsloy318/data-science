#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Jennings Liu@ 2017-06-10 11:04:26

import numpy
temps = [31, 32, 32, 31, 28, 29, 31, 38, 32, 31, 30, 29, 30, 31, 26]
mean=numpy.mean(temps)

print('Mean of temps is %f'%mean)
print('Median of temps is %f'%(numpy.median(temps)))

squared_differences = []
# empty list o squared differences
for temperature in temps:
    difference = temperature - mean
    squared_difference = difference**2
    squared_differences.append(squared_difference)

average_squared_difference = numpy.mean(squared_differences)
standard_deviation = numpy.sqrt(average_squared_difference)
print('mean of squared differences is %f'%average_squared_difference)
print('standard deviation of squared_differences is %f'%standard_deviation)



