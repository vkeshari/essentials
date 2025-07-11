import sys
sys.exit("Reference material. Do not execute.")


### numpy ###
import numpy as np

# Initializers
np.zeros(5)
np.ones((5, 2))
np.array(list(d.values())) # Must convert dict values to list first

# Statistics
data = [1, 2, 3, 4, 5]

np.average(data)
np.std(data)
np.percentile(data, 95, method = 'nearest') # discrete values, also ['lower', 'higher']
np.percentile(data, 95) # continuous values (method = 'linear')

# Checks
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape # --> (2, 3)
a.size # --> 6

# Indices of sorted elements
a = [1, 3, 4, 2, 5]
np.argsort(a) # --> [0, 3, 1, 2, 4]
np.argsort(a)[ : : -1] # --> [4, 2, 1, 3, 0] (reverse sort)

### Array manipulation ###

# Array with repeated elements
np.repeat(1, 3) # --> [1, 1, 1] -- same as [1] * 5 for lists

# Join or extend arrays
np.append([1, 2], [3, 4], axis = 0) # --> [1, 2, 3, 4] -- same as [1, 2] + [3, 4] for lists
np.concatenate(([1, 2], [3, 4], (5, 6))) # --> [1, 2, 3, 4, 5, 6] (allows a tuple of arrays)

# Split an array
np.array_split([1, 2, 3, 4, 5], 3) # --> [[1, 2], [3, 4], [5]]


### numpy matrices ###

# Make a matrix from 1-d arrays
matrix = np.vstack(([1, 2], [3, 4])) # --> [[1, 2], [3, 4]]  -- same as [[1, 2]].append([3, 4])

# Make a 1-d array from a matrix
matrix.flatten() # --> [1, 2, 3, 4]

# Slices of a matrix
matrix[ : , 0] # --> [1, 3]
matrix[ : , 1] # --> [2, 4]

# Transpose a matrix
m = np.array([(1, 2, 3), (4, 5, 6)]) # 2x3
np.transpose(m) # --> [[1, 4], [2, 5], [3, 6]]

# Reshape a matrix
m = np.array([(1, 2, 3), (4, 5, 6)]) # 2x3

# -1 means ignore this dimension, reshape to fit the others
m.reshape(-1, 1) # --> 6x1
m.reshape(1, -1) # --> 1x6
m.reshape(-1, 2) # --> 3x2


### numpy float ranges ###

# Floating point range by step
np.arange(0, 2, 0.5) # --> [0.0, 0.5, 1.0, 1.5]
np.arange(0.1, 1.5, 0.3) # --> [0.1, 0.4, 0.7, 1.0, 1.3]

# Floating point range by bins
#   arguments are min_val, max_val, stops -- max_val included, no. of bins is (stops - 1)
np.linspace(0, 10, 6) # --> [0, 2, 4, 6, 8, 10]
np.linspace((0, 0), (10, 20), 3) # --> [[0, 0], [5, 10], [10, 20]]

# Split a range without rounding errors
bins = round((max_val - min_val) / step)
np.linspace(min_val, max_val, bins + 1)


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

rng.integers(10) # in [0, high)
rng.integers(low = 0, high = 10, size = (2, 3))

rng.choice(['a', 'b', 'c'], size = (2, 3), replace = False)
# replace = True by default, will pick repeated values.

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

# Correlation
vals1 = [1, 2, 3, 4]
vals2 = [4, 3, 2, 1]

p = stats.pearsonr(vals1, vals2)
p.statistic
p.pvalue

s_stat, s_pval = stats.spearmanr(vals1, vals2)
r_stat, r_pval = stats.kendalltau(vals1, vals2)


### scipy.interpolate ###
from scipy import interpolate

# Spline interpolation
tck = interpolate.splrep(xs, ys, k = 3) # 3: cubic spline
ys_new = interpolate.splev(xs_new, tck)

# Monotonic spline interpolation (cubic hermite)
ys_new = interpolate.pchip_interpolate(xs, ys, xs_new)


### scipy.optimize ###
from scipy.optimize import curve_fit, linear_sum_assignment

# Fit an exponential curve
def exp_func(x, a, b, c):
  return a + b * np.exp(-x / c)

(a, b, c), _ = curve_fit(self.exp_func, xs, ys)
ys_new = [exp_func(x, a, b, c) for x in xs_new]

# Assignment matching
cost_matrix = [[0.1, 0.8], [0.5, 0.7]]
(rows, cols) = linear_sum_assignment(cost_matrix, maximize = False) # --> [0, 1] and [1, 0]


### sklearn : 1-d clustering ###
from sklearn.neighbors import KernelDensity

bandwidth = (max(data) - min(data)) / buckets
x_new = np.linspace(min(data), max(data), buckets + 1)
kd = KernelDensity(kernel = 'gaussian', bandwidth = bandwidth)
kde = kd.fit(data.reshape(-1, 1))
y_est = kde.score_samples(x_new.reshape(-1, 1))


### sklearn : Make data more gaussian-like ###
from sklearn.preprocessing import power_transform

data = np.array([1, 2, 3, 4, 5]).reshape(-1, 1) # distribution(s) must be in columns
power_transform(data).reshape(1, -1).flatten()


### fitter : Check which distribution fits data ###
from fitter import Fitter

f = Fitter(data)
f.fit()
print (f.summary(Nbest = 10))


### sklearn : Principal component analysis ###
from sklearn.decomposition import PCA

dataset = [[1, 2, 3, 4], [5, 6, 7, 8]] # 2 points in 4 dimensions
pca = PCA(n_components = 4)
pca.fit(dataset)
pca.explained_variance_ratio_ # Variance ratios along each principal axis (sum = 1)

# Dimensionality reduction
pca = PCA(n_components = 2)
pca.fit(dataset)
pca.transform(dataset)
# Alternative combined fit and transform
pca.fit_transform(dataset)

retained_variance = sum(pca.explained_variance_ratio_)
pca.components_ # Principal axes component vectors (n_components x n_features matrix)
