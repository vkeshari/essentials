import sys
sys.exit("Reference material. Do not execute.")

### scipy.interpolate ###
from scipy import interpolate

# Spline interpolation
tck = interpolate.splrep(xs, ys, k = 3) # 3: cubic spline
y_new = interpolate.splev(x_new, tck)

# Monotonic spline interpolation (cubic hermite)
ys_new = interpolate.pchip_interpolate(xs, ys, xs_new)


### scipy.optimize ###
import numpy as np
from scipy import optimize

# Fit an exponential curve
def exp_func(x, a, b, c):
  return a + b * np.exp(-x / c)

(a, b, c), _ = optimize.curve_fit(self.exp_curve_fit_func, xs, ys)
ys_new = [exp_func(x, a, b, c) for x in xs_new]
