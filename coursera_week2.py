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




