# Pandas visualisation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# lets take a look at the matplotlib's style package.
# Matplotlib comes with a number of predefined styles, which we can choose from, to change the default look of our plots
# Because pandas is using matplotlib under the hood, this will change the default style of our pandas graphs as well.

# see the pre-defined styles provided.
plt.style.available

# Let's use the seaborn-colorblind style, which will change the default colors of our plots to use a color palette that
# is more color vision deficiency friendly.

# use the 'seaborn-colorblind' style
plt.style.use('seaborn-colorblind')

# Let's make a DataFrame. First, we'll set the seed for the random number generator, which will allow us to reproduce
# the data.
# Next, let's add three columns of random time series data.
# We can generate the random data by cumulatively summing up random numbers.
# numpi has a great function for this called cumsum, which cumulatively sums an array
# Let's do this for three columns, A, B and C. And also offset the B column by + 20 and the C column by- 20. Using
# date_range, we can set the index to be everyday in 2017.

np.random.seed(123)

df = pd.DataFrame({'A': np.random.randn(365).cumsum(0),
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20},
                  index=pd.date_range('1/1/2017', periods=365))
df

df.plot() # add a semi-colon to the end of the plotting call to suppress unwanted output

# We can select which plot we want to use by passing it into the 'kind' parameter.

df.plot('A','B', kind = 'scatter')

# You can also choose the plot kind by using the DataFrame.plot.kind methods instead of providing the kind keyword argument.

# kind :

# 'line' : line plot (default)
# 'bar' : vertical bar plot
# 'barh' : horizontal bar plot
# 'hist' : histogram
# 'box' : boxplot
# 'kde' : Kernel Density Estimation plot
# 'density' : same as 'kde'
# 'area' : area plot
# 'pie' : pie plot
# 'scatter' : scatter plot
# 'hexbin' : hexbin plot

# This time we want to make a scatterplot with points varying in color and size. We'll use df.plot.scatter, pass in
# columns A and C.
# And set the color C and size S to change based on the value of column B.
# Finally, we can choose the color palette used by passing a string into the parameter color map.
# Here, I'll use viridis, which is particularly pleasing to the eye.

# create a scatter plot of columns 'A' and 'C', with changing color (c) and size (s) based on column 'B'
df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')

ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
ax.set_aspect('equal')

df.plot.box();

df.plot.hist(alpha=0.7);

# Kernel density estimation plots are useful for deriving a smooth continuous function from a given sample.
df.plot.kde();

iris = pd.read_csv('IRIS.csv')
iris.head()

pd.plotting.scatter_matrix(iris);

plt.figure()
pd.tools.plotting.parallel_coordinates(iris, 'species');
