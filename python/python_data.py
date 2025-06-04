import sys
sys.exit("Reference material. Do not execute.")


### numpy ###
import numpy as np

# Initializers
np.zeros(5)
np.ones((5, 2))
np.array(list(d.values())) # Must convert dict values to list first

# Statistics
np.average(data)
np.std(data)
np.percentile(date, 95, method = 'nearest') # discrete values, also ['lower', 'higher']
np.percentile(date, 95) # continuous values (method = 'linear')


### numpy histograms ###

# 3 bins with borders at [1, 2), [2, 3) and [3, 4]
bins = [1, 2, 3, 4]
nums = [1, 2, 3, 4, 5]
reps = [1, 2, 1, 2, 2]

# Count values in bins
np.histogram(nums, bins = bins) # --> [[1, 1, 2], [1, 2, 3, 4]]

np.histogram(reps, bins = bins) # --> [[2, 3, 0], [1, 2, 3, 4]]
np.histogram(reps, bins = bins, density = True) # --> [[0.4, 0.6, 0.0], [1, 2, 3, 4]]

bin_counts = np.histogram(nums, bins = bins)[0]

# Histogram percentiles (returns discrete values)
bins_shifted = [b + bin_width / 2 for b in bins]
np.percentile(a = bins_shifted, q = 95, weights = bin_counts, method = 'inverted_cdf')

# Which bin does each value go into (examples below)
np.digitize(nums, bins, right = False) # Only works for numbers
np.searchsorted(bins, nums, side = 'left') # side in ['left', 'right']

values = [1, 2, 3, 4, 5, 6]
bins = [3, 5]

# Match [lower, upper)
bin_mapping = np.digitize(x = values, bins = bins, right = False)   # --> [0, 0, 1, 1, 2, 2] *
bin_mapping = np.searchsorted(a = bins, v = values, side = 'right') # --> [0, 0, 1, 1, 2, 2] *

# Match (lower, upper]
bin_mapping = np.digitize(x = values, bins = bins, right = True)   # --> [0, 0, 0, 1, 1, 2] *
bin_mapping = np.searchsorted(a = bins, v = values, side = 'left') # --> [0, 0, 0, 1, 1, 2] *

# * --> Subtract 1 for actual bin indices
bin_mapping = [b - 1 for b in bin_mapping]


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


### numpy matrices ###

# Transpose a matrix
m = np.array([(1,2,3),(4,5,6)]) # 2x3
np.transpose(m) # --> [(1,4),(2,5),(3,6)]

# Reshape a matrix
m = np.array([(1,2,3),(4,5,6)]) # 2x3
m.reshape(-1, 1) # --> 6x1
m.reshape(1, -1) # --> 1x6
m.reshape(-1, 2) # --> 3x2


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


### scipy.stats ###
from scipy import stats

stats.describe(data) # returns (nobs, minmax, mean, variance, skewness, kurtosis)

stats.skew(data)
stats.kurtosis(data)

# Percentiles and reverse-percentiles in data
stats.percentileofscore(data, 0.5)
stats.scoreatpercentile(data, 50)
# Both methods will average / interpolate.


### scipy.interpolate ###
from scipy import interpolate

# Spline interpolation
tck = interpolate.splrep(xs, ys, k = 3) # 3: cubic spline
ys_new = interpolate.splev(xs_new, tck)

# Monotonic spline interpolation (cubic hermite)
ys_new = interpolate.pchip_interpolate(xs, ys, xs_new)


### scipy.optimize ###
from scipy.optimize import curve_fit

# Fit an exponential curve
def exp_func(x, a, b, c):
  return a + b * np.exp(-x / c)

(a, b, c), _ = curve_fit(self.exp_func, xs, ys)
ys_new = [exp_func(x, a, b, c) for x in xs_new]


### sklearn : 1-d clustering ###
from sklearn.neighbors import KernelDensity

bandwidth = (max(data) - min(data)) / buckets
x_new = np.linspace(min(data), max(data), buckets + 1)
kd = KernelDensity(kernel = 'gaussian', bandwidth = bandwidth)
kde = kd.fit(data.reshape(-1, 1))
y_est = kde.score_samples(x_new.reshape(-1, 1))


### sklearn : Reshape 1-d distribution ###
from sklearn.preprocessing import power_transform

power_transform(data.reshape(-1, 1)).reshape(1, -1).flatten()


### fitter : Check which distribution fits data ###
from fitter import Fitter

f = Fitter(data)
f.fit()
print (f.summary(Nbest = 10))
