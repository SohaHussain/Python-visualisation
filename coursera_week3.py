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

# Box and Whisker plots

# A box plot. Sometimes called a box-and-whisker plot is a method of showing aggregate statistics of various samples
# in a concise matter.
# The box plot simultaneously shows, for each sample, the median of each value, the minimum and maximum of the samples,
# and the interquartile range.

import pandas as pd
normal_sample = np.random.normal(loc=0.0, scale=1.0, size=10000)
random_sample = np.random.random(size=10000)
gamma_sample = np.random.gamma(2, size=10000)

df = pd.DataFrame({'normal': normal_sample,
                   'random': random_sample,
                   'gamma': gamma_sample})

df.describe()

# Like standard deviation, the interquartile range is a measure of variability of data. And it's common to plot this
# using a box plot.

# In a box plot, the mean, or the median, of the data is plotted as a straight line. Two boxes are formed, one above,
# which represents the 50% to 75% data group, and one below, which represents the 25% to 50% data group. Thin lines
# which are capped are then drawn out to the minimum and maximum values.

# Like standard deviation, the interquartile range is a measure of variability of data. And it's common to plot this using a box plot.
#
# In a box plot, the mean, or the median, of the data is plotted as a straight line. Two boxes are formed, one above,
# which represents the 50% to 75% data group, and one below, which represents the 25% to 50% data group. Thin lines
# which are capped are then drawn out to the minimum and maximum values.

plt.figure()
# create a boxplot of the normal data, assign the output to a variable to supress output
_ = plt.boxplot(df['normal'], whis=10000.0)
# whis tells the box plot to set the whisker values all the way out to the minimum and maximum values

# clear the current figure
plt.clf()
# plot boxplots for all three of df's columns
_ = plt.boxplot([ df['normal'], df['random'], df['gamma'] ], whis=10000.0)

# if we look at the gamma distribution, for instance, we see the tail of it is very, very long. So the maximum values
# are very far out.

plt.figure()
_ = plt.hist(df['gamma'], bins=100)

# We can actually overlay an axes on top of another within a figure. Now, this functionality isn't in the basic
# matplotlib space, but it's in the toolkits, which tend to ship with matplotlib.
#
# The toolkit that we're going to use is called the axes grid, and we import it from the
# mpl_toolkits.axes_grid1.inset_locator.

# We create a new figure and we put up our box plot.
#
# Then we just call the inset locator and pass it the current axes object we want composition on top of, followed by the
# size of our new axis. And we can specify this as both a width and a height in percentage from the parent axes. Then we
# give it a number from the place in which we wanted to drop the new axes.

import mpl_toolkits.axes_grid1.inset_locator as mpl_il

plt.figure()
plt.boxplot([ df['normal'], df['random'], df['gamma'] ], whis=10000.0)
# overlay axis on top of another
ax2 = mpl_il.inset_axes(plt.gca(), width='60%', height='40%', loc=2)
ax2.hist(df['gamma'], bins=100)
ax2.margins(x=0.5)

# switch the y axis ticks for ax2 to the right side
ax2.yaxis.tick_right()

# if `whis` argument isn't passed, boxplot defaults to showing 1.5*interquartile (IQR) whiskers with outliers
plt.figure()
_ = plt.boxplot([ df['normal'], df['random'], df['gamma'] ] )

# Heatmaps

# Heatmaps are a way to visualize three-dimensional data and to take advantage of spatial proximity of those dimensions.

plt.figure()

Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
_ = plt.hist2d(X, Y, bins=25)

plt.figure()
_ = plt.hist2d(X, Y, bins=100)

# add a colorbar legend
plt.colorbar()



