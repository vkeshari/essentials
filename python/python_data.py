import sys
sys.exit("Reference material. Do not execute.")


### numpy ###
import numpy as np

# Initializers
np.zeros(5)
np.ones((5, 2))

# Statistics
np.average(data)
np.percentile(date, 95, method = 'nearest') # discrete values, also ['lower', 'higher']
np.percentile(date, 95) # continuous values (method = 'linear')

np.histogram([1, 2, 1, 2, 2], bins = [1, 2, 3]) # --> [[2, 3], [1, 2, 3]]
np.histogram([1, 2, 1, 2, 2], bins = [1, 2, 3], density = True) # --> [[0.4, 0.6], [1, 2, 3]]


### numpy float ranges ###

# Floating point range by step
np.arange(0, 2, 0.5) # --> [0.0, 0.5, 1.0, 1.5]
np.arange(0.1, 1.5, 0.3) # --> [0.1, 0.4, 0.7, 1.0, 1.3]

# Floating point range by bins
np.linspace(min_val, max_val, bins) # includes max_val
np.linspace(0, 10, 6) # --> [0, 2, 4, 6, 8, 10]
np.linspace((0, 0), (10, 20), 3) # --> [[0, 0], [5, 10], [10, 20]]

# Split a range without rounding errors
bins = round((max_val - min_val) / step)
np.linspace(min_val, max_val, bins + 1)


### numpy.random ###

# Random numbers
np.random.rand()
np.random.rand(3) # array
np.random.rand(2, 3) # matrix

np.random.randint(10)
np.random.randint(low = 0, high = 10, size = (2, 3))

# Random number generator
rng = np.random.default_rng()
rng = np.random.default_rng(seed = 100)
rng = np.random.default_rng(seed = [1, 2, 3])

rng.random()
rng.random(size = (2, 3))

rng.integer(10)
rng.integer(low = 0, high = 10, size = (2, 3))

rng.choice(['a', 'b', 'c'], size = (2, 3))
rng.shuffle(['a', 'b', 'c']) # shuffles in-place

# Distributions
np.random.uniform()
np.random.uniform(low = 0, high = 10, size = 10) # high included

np.random.normal() # or standard_normal()
np.random.normal(loc = 5, scale = 1, size = 10) # loc is mean, scale is std
# Distributions: https://numpy.org/doc/stable/reference/random/generator.html#distributions


### scipy.interpolate ###
from scipy import interpolate

# Spline interpolation
tck = interpolate.splrep(xs, ys, k = 3) # 3: cubic spline
y_new = interpolate.splev(x_new, tck)

# Monotonic spline interpolation (cubic hermite)
ys_new = interpolate.pchip_interpolate(xs, ys, xs_new)


### scipy.optimize ###
from scipy import optimize

# Fit an exponential curve
def exp_func(x, a, b, c):
  return a + b * np.exp(-x / c)

(a, b, c), _ = optimize.curve_fit(self.exp_func, xs, ys)
ys_new = [exp_func(x, a, b, c) for x in xs_new]
