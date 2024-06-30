import sys
sys.exit("Reference material. Do not execute.")


### numpy ###
import numpy as np

np.average(data)
np.percentile(date, 95, method = 'nearest') # or use method = 'linear' for continuous

# Floating point range by step
np.arange(min_val, max_val, step) # excludes max_val like range
np.arange(0, 2, 0.5) # --> [0.0, 0.5, 1.0, 1.5]
np.arange(0.1, 1.5, 0.3) # --> [0.1, 0.4, 0.7, 1.0, 1.3]

# Floating point range by bins
np.linspace(min_val, max_val, bins) # includes max_val
np.linspace(0, 10, 6) # --> [0, 2, 4, 6, 8, 10]
np.linspace((0, 0), (10, 20), 3) # --> [[0, 0], [5, 10], [10, 20]]

# Split a range without rounding errors
bins = round((max_val - min_val) / step)
np.linspace(min_val, max_val, bins)


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
