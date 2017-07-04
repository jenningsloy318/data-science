#!/usr/bin/python
import numpy as np
from matplotlib import pyplot as plt

def normal_pdf(x, mu = 5, sigma = 1):
    return (1./np.sqrt(2*3.14 * sigma**2)) * 2.718**(-(x-mu)**2 / (2.* sigma**2))

x_values = np.linspace(-20,20,100)
y_values = [normal_pdf(x) for x in x_values]
plt.plot(x_values, y_values)
plt.title("Normal PDF")
plt.show()