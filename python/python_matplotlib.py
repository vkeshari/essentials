import sys
sys.exit("Reference material. Do not execute.")


### Plot setup ###
from matplotlib import pyplot as plt

resolution = tuple([19.2, 10.8]) # 1920 x 1080

# Single plot
fig, ax = plt.subplots(figsize = resolution)

# Multiple plots
fig, axs = plt.subplots(nrows = 2, ncols = 3, \
                            sharex = True, sharey = False, \ # Share subplot properties
                            width_ratios = [1, 2, 3], \ # Relative subplot dimensions
                            height_ratios = [2, 3], \
                          )
# axs === ((ax11, ax12, ax13), (ax21, ax22, ax23))

fig.tight_layout()

# Show or save
plt.show()
fig.savefig(filename)


### Animation ###
from matplotlib import animation

def draw_frame(frame):
  axs.clear()
  # ...
  plt.draw()

writer = animation.FFMpegWriter(fps = 60, bitrate = 5000)
with writer.saving(fig, filename, dpi = 100):
  for frame in range(1, 1000):
    draw_frame(frame)
    writer.grab_frame()


### Annotations ###

# Title
ax.set_title(title_text, fontsize ='xx-large', fontweight='bold')

# Axes label
ax.set_ylabel(ylabel, fontsize ='x-large', style = 'italic')

# Axes limits and labels
plt.yscale('log') # or default 'linear', do this before setting ticks and labels
ax.set_ylim(0, 100) # doesn't work for log scale
yticks = range(0, 100, 10)
ax.set_yticks(yticks)
ax.set_yticklabels([str(y) for y in yticks], fontsize ='large')

# Axes grid
ax.grid(True, which = 'both', axis = 'x', alpha = 0.5)
# which in ['major', 'minor', 'both']
# axis in ['x', 'y', 'both']

# Horizontal and vertical lines
plt.axhline(y = 50, xmin = 0, xmax = 0.9, linestyle = ':', linewidth = 5)
plt.axvline(x = 1000, ymin = 0.1, color = 'grey', alpha = 0.5, linestyle = '--')

# Text
plt.text(x = 50, y = 1000, s = str(date), rotation = 45, \
              alpha = 0.8, fontsize = 'medium', \
              horizontalalignment = 'left', \ # ['left', 'right', 'center']
              verticalalignment = 'top', \ # ['top', 'bottom', 'center']
            )


### Colors ###
from matplotlib import cm

# Assign a named color
mycolor = 'lightgrey'
# Named colors: https://matplotlib.org/stable/gallery/color/named_colors.html

# Assign a colormap
cmap = 'rainbow'
cmap_reverse = 'rainbow_r'
# Colormaps: https://matplotlib.org/stable/users/explain/colors/colormaps.html

# Sample N colors from colorscale
for i in range(len(data)): # or use numpy.linscale()
  color_stops.append(i / len(data))
colors = cm.rainbow(color_stops)


### Legend ###

# Provide labels
ax.legend(labels = labs, loc = 'lower right', fontsize = 'medium')
# loc in ['upper left', 'center right', 'lower center', 'best', ...]

# Use assigned labels
line1, _ = ax.plot([1, 2], [1, 2], label = 'RED TEAM')
line2, _ = ax.plot([3, 4], [4, 3], label = 'BLUE TEAM')
ax.legend(handles = [line1, line2])

# Colorbar with labels
cbar = plt.colorbar(line1,
                      shrink = 0.75, aspect = 50, \ # aspect is y / x
                      format = "%d", pad = 0.01, \
                      ticks = [1, 2, 5, 10] \
                    )
cbar.ax.tick_params(labelsize = 'medium')
cbar.set_label('No. of players', 'large')


### Graph Types ###

# Line Chart
plt.plot(xs, ys, \
            linestyle = '-', linewidth = 5, antialiased = True, \
            alpha = 0.5, color = 'darkgrey', \
            )
# linestyle in ['', '-', '--', ':', '-.']

plt.plot(xs, ys, \
            marker = "o", markersize = 5, \
            alpha = 0.5, color = 'orangered', \
            )
# Markers: https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers

# Scatterplot
plt.scatter(xs, ys, s = sizes, c = cols, \
                marker = None, alpha = 0.5, \
              )

# Bar
ax.bar(xs, ys, width = 10, align = 'edge', \ # align in ['center', 'edge']
        color = color, alpha = 0.7)

# Horizontal Bars
ax.barh(y = y_coords, width = vals, align = 'center', \ # align in ['center', 'edge']
          height = 0.9, left = start_vals, \
          color = cols, alpha = 0.6, \
        )

# Histogram
ax.hist(data, bins = 10, \
          cumulative = False, range = (0, 100), \ # only data in range is plotted
          align = 'mid', \ # align in ['left', 'right', 'mid']
          orientation = 'vertical', \ # orientation in ['horizontal', 'vertical']
          label = label, color = 'blue', alpha = 0.6)

# Histogram with unequal bins
ax.hist(data, bins = [0, 20, 80, 100], \ # --> bins are [0, 20), [20, 80), [80, 100]
          label = label, color = 'red', alpha = 0.4)


### Image ###
import matplotlib.image as mpimg

# Read image
img = mpimg.imread(filename)

# Show image
fig_extents = [x_min, x_max, y_min, y_max]
fig_aratio = 1.5 # aspect ratio scales pixels and is y / x, or in ['equal', 'auto']
ax.imshow(img, extent = fig_extents, aspect = fig_aratio, alpha = 1.0, \
            cmap='viridis', vmin = 0, vmax = 255, \ # [vmin, vmax] is range of data to plot
          )
