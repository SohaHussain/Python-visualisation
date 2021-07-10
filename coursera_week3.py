# Subplots

import matplotlib.pyplot as plt
import numpy as np

# If we look at the subplot documentation, we see that the first argument is the number of rows, the second the number
# of columns, and the third is the plot number.

# In matplotlib, a conceptual grid is overlayed on the figure. And a subplot command allows you to create axis to
# different portions of this grid.

# For instance, if we want to to create two plots side by side, we would call subplot with the parameters 1, 2, and 1.
# This would allow us to use 1 row, with 2 columns, and set the first axis to be the current axis.

plt.figure()
plt.subplot(1,2,1)
linear_data=np.array([1,2,3,4,5,6,7,8])
plt.plot(linear_data,'-o')

exponential_data = linear_data**2

# subplot with 1 row, 2 columns, and current axis is 2nd subplot axes
plt.subplot(1, 2, 2)
plt.plot(exponential_data, '-o')

# plot exponential data on 1st subplot axes
plt.subplot(1, 2, 1)
plt.plot(exponential_data, '-x')

plt.figure()
# the right hand side is equivalent shorthand syntax
plt.subplot(1,2,1) == plt.subplot(121)

# create a 3x3 grid of subplots
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(3, 3, sharex=True, sharey=True)
# plot the linear_data on the 5th subplot axes
ax5.plot(linear_data, '-')

# set inside tick labels to visible
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)

# necessary on some systems to update the plot
plt.gcf().canvas.draw()

# Histograms

# repeat with number of bins set to 100
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
axs = [ax1,ax2,ax3,ax4]

for n in range(0,len(axs)):
    sample_size = 10**(n+1)
    sample = np.random.normal(loc=0.0, scale=1.0, size=sample_size)
    axs[n].hist(sample, bins=100)
    axs[n].set_title('n={}'.format(sample_size))

# The GridSpec allows you to map axes over multiple cells in a grid.

plt.figure()
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
plt.scatter(X,Y)

# it's not totally clear from looking at this plot what the actual distributions are for each axis, but we could add two
# smaller plots, each histograms, to make this a bit more clear.

# I'm going to define a 3x3 grid, nine cells in total. I want the first histogram to take up the top right space, and
# the second histogram to take up the far left bottom two spaces, rotated on its side.
# The original scatter plot can take up a two by two square in the bottom right.

# When we add new items with the subplot, instead of specifying the three numbers of row, column and position, we pass
# in the elements of the GridSpec object which we wish to cover. And very important here. Because we are using the
# elements of a list, all of the indexing starts at zero, and is very reasonable to use slicing for the beginning or
# ends of lists.

import matplotlib.gridspec as gridspec
plt.figure()
gspec=gridspec.GridSpec(3,3)
top_histogram = plt.subplot(gspec[0, 1:])
side_histogram = plt.subplot(gspec[1:, 0])
lower_right = plt.subplot(gspec[1:, 1:])

Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
lower_right.scatter(X, Y)
top_histogram.hist(X, bins=100)
s = side_histogram.hist(Y, bins=100, orientation='horizontal')

# clear the histograms and plot normed histograms
top_histogram.clear()
top_histogram.hist(X, bins=100)
side_histogram.clear()
side_histogram.hist(Y, bins=100, orientation='horizontal')
# flip the side histogram's x axis
side_histogram.invert_xaxis()

# change axes limits
for ax in [top_histogram, lower_right]:
    ax.set_xlim(0, 1)
for ax in [side_histogram, lower_right]:
    ax.set_ylim(-5, 5)


