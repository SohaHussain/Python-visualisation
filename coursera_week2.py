# BASIC PLOTTING WITH MATPLOTLIB

#  You can show matplotlib figures directly in the notebook by using the %matplotlib notebook and %matplotlib
#  inline magic commands.

# %matplotlib notebook provides an interactive environment.

# So what actually has happened when you run the magic function matplotlib with the inline parameter, is that matplotlib
# is configured to render into the browser. This configuration is called a backend, and matplotlib has a number of
# different backends available. A backend is an abstraction layer which knows how to interact with the operating
# environment, whether it's an operating system, or an environment like the browser, and knows how to render matplotlib
# commands. In fact, there's a number of different interactive backends, but there are also backends called hard copy
# backends, which support rendering to graphics formats, like scalable vector graphics, SVGs, or PNGs.

import matplotlib as mpl
mpl.get_backend()

# The next layer is where we'll spend most of our time though, and that's called the artist layer. The artist layer is
# an abstraction around drawing and layout primitives. The root of visuals is a set of containers which includes a
# figure object with one or more subplots, each with a series of one or more axes. It also contains primitives such as
# Line2D, recatangle and collections such as PathCollection

# there's one more layer which is extremely important for us as data scientists in particular, and this is called the
# scripting layer. if we were writing an application to use matplotlib, we might never care about the scripting layer.
# But this layer helps simplify and speed up our interaction with the environment in order to build plots quickly.
# It does this, frankly, by doing a bunch of magic for us. And the difference between someone who is effective with
# matplotlib and someone who isn't, is usually based on their understanding of this magic of the scripting layer. The
# scripting layer we use in this course is called pyplot.

# The pyplot scripting layer is a procedural method for building a visualization, in that we tell the underlying
# software which drawing actions we want it to take in order to render our data. There are also declarative methods for
# visualizing data. HTML is a great example of this. Instead of issuing command after command to the backend rendering
# agent, which is the browser with HTML, HTML documents are formatted as models of relationships in a document, often
# called the DOM, or Document Object Model. These are two fundamentally different ways of creating and representing
# graphical interfaces.

# The popular JavaScript library, for instance, D3.JS is an example of a declarative information visualization method.
# While matplotlib's pyplot is an example of a procedural information visualization method.

# MAKING GRAPHS USING PLOT FUNCTION

# A plot has two axes, an x-axis along the horizon, and a y-axis which runs vertically.

import matplotlib.pyplot as plt
# supports any number of named and unnamed arguments the arguments will be interpreted as x, y pairs

# because the default is the line style '-',
# nothing will be shown if we only pass in one point (3,2)
plt.plot(3,2)

# we can pass in '.' to plt.plot to indicate that we want
# the point (3,2) to be indicated with a marker '.'
plt.plot(3,2,'.')

# create a new figure
plt.figure()

# plot the point (3,2) using the circle marker
plt.plot(3, 2, 'o')

# get the current axes
ax = plt.gca()

# Set axis properties [xmin, xmax, ymin, ymax]
ax.axis([0,6,0,10])

# create a new figure
plt.figure()

# plot the point (1.5, 1.5) using the circle marker
plt.plot(1.5, 1.5, 'o')
# plot the point (2, 2) using the circle marker
plt.plot(2, 2, 'o')
# plot the point (2.5, 2.5) using the circle marker
plt.plot(2.5, 2.5, 'o')

# we can go further with the axes object to the point where we can actually get all of the child objects that that axes
# contains. We do this with the axes get_children function.

# get current axes
ax = plt.gca()
# get all the child objects the axes contains
ax.get_children()

# Here, we can see that there's actually three line to the objects contained in this axes, these are our data points.
# A number of spines which are actual renderings of the borders of the frame including tic markers, two axis objects,
# and a bunch of text which are the labels for the chart. There's even a rectangle which is the background for the axes.

# Scatterplots

# A scatterplot is a two dimensional plot similar to the line plots I've shown. The scatter function takes an x-axis
# value as a first argument and y-axis value as the second. If the two arguments are the same, we get a nice diagonal
# alignment of points.

import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
y=x
plt.figure()
plt.scatter(x,y)
# similar to  plt.plot(x, y, '.'), but the underlying child objects in the axes are not Line2D

import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x

# create a list of colors for each point to have
# ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'red']
colors = ['green']*(len(x)-1)
colors.append('red')

plt.figure()

# plot the point with size 100 and chosen colors
plt.scatter(x, y, s=100, c=colors)

# convert the two lists into a list of pairwise tuples
zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])

print(list(zip_generator))
# the above prints:
# [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
# The single star * unpacks a collection into positional arguments
print(*zip_generator)
# the above prints:
# (1, 6) (2, 7) (3, 8) (4, 9) (5, 10)

# use zip to convert 5 tuples with 2 elements each to 2 tuples with 5 elements each
print(list(zip((1, 6), (2, 7), (3, 8), (4, 9), (5, 10))))
# the above prints:
# [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)]


zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
# let's turn the data back into 2 lists
x, y = zip(*zip_generator) # This is like calling zip((1, 6), (2, 7), (3, 8), (4, 9), (5, 10))
print(x)
print(y)
# the above prints:
# (1, 2, 3, 4, 5)
# (6, 7, 8, 9, 10)

plt.figure()
# plot a data series 'Tall students' in red using the first two elements of x and y
plt.scatter(x[:2], y[:2], s=100, c='red', label='Tall students')
# plot a second data series 'Short students' in blue using the last three elements of x and y
plt.scatter(x[2:], y[2:], s=100, c='blue', label='Short students')

# add a label to the x axis
plt.xlabel('The number of times the child kicked a ball')
# add a label to the y axis
plt.ylabel('The grade of the student')
# add a title
plt.title('Relationship between ball kicking and grades')

# add a legend (uses the labels from plt.scatter)
plt.legend()

# add the legend to loc=4 (the lower right hand corner), also gets rid of the frame and adds a title
plt.legend(loc=4, frameon=False, title='Legend')






