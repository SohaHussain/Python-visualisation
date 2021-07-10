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

