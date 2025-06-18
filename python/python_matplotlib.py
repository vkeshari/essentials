import sys
sys.exit("Reference material. Do not execute.")

from pathlib import Path

### Plot setup ###
from matplotlib import pyplot as plt

resolution = tuple([19.2, 10.8]) # 1920 x 1080

# Single plot
fig, ax = plt.subplots(figsize = resolution)

# Multiple plots
fig, axs = plt.subplots(nrows = 2, ncols = 3,
                            sharex = True, sharey = False, # Share subplot properties
                            width_ratios = [1, 2, 3], # Relative subplot dimensions
                            height_ratios = [2, 3],
                          )
# axs === ((ax11, ax12, ax13), (ax21, ax22, ax23))


# Show plot
fig.tight_layout()
plt.show()

# Save plot
fig.tight_layout()
filename = Path("graphs/out_graph.png")
filename.parent.mkdir(exist_ok = True, parents = True)
fig.savefig(filename)
plt.close()


### Animation ###
from matplotlib import animation

def draw_frame(frame):
  axs.clear()
  # ...
  plt.draw()

writer = animation.FFMpegWriter(fps = 60, bitrate = 5000)
filename = Path("graphs/out_animation.mpg")
filename.parent.mkdir(exist_ok = True, parents = True)
with writer.saving(fig, filename, dpi = 100):
  for frame in range(1, 1000):
    draw_frame(frame)
    writer.grab_frame()


### Annotations ###

# Title
ax.set_title(title_text, fontsize = 'xx-large', fontweight='bold')

# Axes label
ax.set_ylabel(ylabel, fontsize = 'x-large', style = 'italic')

# Axes limits and labels
plt.yscale('log') # or default 'linear', do this before setting ticks and labels
ax.set_ylim(0, 100) # doesn't work for log scale

yticks_major = range(0, 100, 10)
yticks_minor = range(0, 100)

ax.set_yticks(yticks)
ax.set_yticks(yticks, minor = True)

ax.set_yticklabels([str(y) for y in yticks_major], fontsize ='large')

# Axes grid
ax.grid(True, which = 'both', axis = 'both', alpha = 0.5)
# which in ['major', 'minor', 'both']
# axis in ['x', 'y', 'both']
# set different alphas for major and minor ticks

# Text
plt.text(x = 50, y = 1000, s = str(date), rotation = 45, # both x and y are in coordinate space
              alpha = 0.8, fontsize = 'medium',
              horizontalalignment = 'left', # ['left', 'right', 'center']
              verticalalignment = 'top', # ['top', 'bottom', 'center']
            )

# Horizontal and vertical lines
# Position is in coordinate space but bounds are in graph space: (0, 1)
plt.axhline(y = 50, xmin = 0, xmax = 0.9, linestyle = ':', linewidth = 5)
plt.axvline(x = 1000, ymin = 0.1, color = 'grey', alpha = 0.5, linestyle = '--')

# Shapes
from matplotlib.patches import Rectangle

ax.add_patch(Rectangle((x0, y0), height = 1, width = 1, edgecolor = 'red', facecolor = 'green',
                          linewidth = 2, alpha = 1.0, fill = True))


### Colors ###
from matplotlib import cm, colors

# Assign a named color
mycolor = 'darkgrey'
# Named colors: https://matplotlib.org/stable/gallery/color/named_colors.html

# Get named color lists
list(colors.TABLEAU_COLORS.keys()) # 10 tableau colors (default)
list(colors.CSS4_COLORS.keys()) # 148 CSS4 colors -- shuffle recommended

# Assign a colormap
cmap = 'turbo'
cmap_reverse = 'jet_r'
# Colormaps: https://matplotlib.org/stable/users/explain/colors/colormaps.html

# Sample N colors from colorscale
color_stops = np.linspace(0, 1, num_colors + 1)
colors = cm.brg(color_stops)


### Legend ###

# Provide labels
ax.legend(labels = labs, loc = 'best', fontsize = 'medium')
# loc in ['best', 'upper left', 'center right', 'lower center', ...]

# Use assigned labels
line1, _ = ax.plot([1, 2], [1, 2], label = 'RED TEAM')
line2, _ = ax.plot([3, 4], [4, 3], label = 'BLUE TEAM')
ax.legend(handles = [line1, line2])

# Colorbar with labels
cbar = plt.colorbar(line1,
                      shrink = 0.75, aspect = 50, # aspect is y / x
                      format = "%d", pad = 0.01,
                      ticks = [1, 2, 5, 10],
                    )
cbar.set_label('No. of players', size = 'large')

cbar.ax.tick_params(labelsize = 'medium')
cbar.ax.set_yticklabels([str(t) for t in ticks], fontsize = 'medium')


### Graph Types ###

# Line Chart
plt.plot(xs, ys, \
            linestyle = '-', linewidth = 5, antialiased = True,
            alpha = 0.5, color = 'darkgrey',
            )
# linestyle in ['', '-', '--', ':', '-.']

plt.plot(xs, ys, \
            marker = "o", markersize = 5,
            alpha = 0.5, markeredgecolor = 'orangered',
            )
# Markers: https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers

# Scatterplot
plt.scatter(xs, ys, s = sizes, c = cols,
                marker = None, alpha = 0.5,
              )

# Bar
ax.bar(xs, ys, width = 10, align = 'edge', # align in ['center', 'edge']
        color = color, alpha = 0.7, linewidth = 1, edgecolor = 'darkgrey')

# Horizontal Bars
ax.barh(y = y_coords, width = vals, align = 'center', # align in ['center', 'edge']
          height = 0.9, left = start_vals,
          color = cols, alpha = 0.6,
        )

# Histogram
ax.hist(data, bins = 10, \
          cumulative = False, range = (0, 100), # only data in range is plotted
          align = 'mid', # align in ['left', 'right', 'mid']
          orientation = 'vertical', # orientation in ['horizontal', 'vertical']
          label = label, color = 'blue', alpha = 0.6)

# Histogram with unequal bins
ax.hist(data, bins = [0, 20, 80, 100], # --> bins are [0, 20), [20, 80), [80, 100]
          label = label, color = 'red', alpha = 0.4)

# Heatmap
# By default, origin is 'upper' (like scan line printing an image)
# aspect can be a float (ratio of the scale of axes)
#   e.g. if x-axis is in [0, 1] and y-axis is in [0, 10], aspect should be 0.1 for square image
plt.imshow(xy, origin = 'lower', aspect = 'auto', # aspect in ['equal', 'auto'] or float
              extent = (xmin, xmax, ymin, ymax),
              cmap = 'viridis', vmin = 0, vmax = 1) # [vmin, vmax] is range of data to plot

# Contours
plt.contour(xy, levels = range(0, 10), colors = 'white', # or list of colors
              alpha = 0.5, antialiased = True)


### Image ###
import matplotlib.image as mpimg

# Read image
img = mpimg.imread(filename)

# Show image
fig_extents = [x_min, x_max, y_min, y_max]
fig_aratio = 1.5 # aspect ratio scales pixels and is y / x, or in ['equal', 'auto']
ax.imshow(img, extent = fig_extents, aspect = fig_aratio, alpha = 1.0)
