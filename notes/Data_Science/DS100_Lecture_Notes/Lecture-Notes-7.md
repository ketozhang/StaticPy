---
title: Lecture Notes7
---
# Lecture Notes 7 - Data Visualization

> **Motivation:** While looking at numerical data in a table may be useful, there are occasion where visualizing data can bring more information (even more accurate).

## Matplotlib

Matplotlib (`matplotlib`) is a very popular Python package and is considered a essential tool for visualization. 

Specifically, the Pyplot of Matplotlib (`matplotlib.pyplot`) is used for plotting data points (not functions like in Mathematica). 

```python
%matplotlib inline # only for Jupyter Notebook
%matplotlib notebook # enable interactive plotting for Jupyter Notebook
import matplotlib.pyplot as plt
```

Typical use of plotting (notice we do not use symbolic expression, everything must be numerical such that we require an array of points):

```python
# Plotting sin(x)
x = np.linspace(0, 2*np.pi, 300) # create 300 data points from 0 to 2*pi
y = np.sin(x)

# Create a plot
plt.plot(x, y, label=r'$\sin(x)$')

# Add some information to the plot
plt.xlabel('x') # set x-axis label
plt.ylabel('y') # set y-axis label
plt.title('Some Functions') # set plot title
plt.grid() # turn on grids
plt.legend() # turn on legend otherwise label argument from plt.plot does not show

plot.show() # optional in Jupyter, required in Python to bring up a window for the plot.
```

### Color Maps
A color map is one that is useful in drawing 3D data onto a 2D plane with color being the 3rd dimension. Think of some 3D distribution $z(x,y)$ where $z$ is the 3rd dimension.

$$ \text{Color Value} = z(x,y) $$

* Do not use the full spectrum of RGB to convey a 2D array (3D plot)
    * Causes problems because the middle of the RGB spectrum is much brighter to humans than the edges (red and blue)
    * Those who are color blind have a difficult time reading RGB colormaps.
    * Viridis and many other colormaps were made to sovle this problem.
* Some color maps are best for certain data ([see color maps for oceanography](https://matplotlib.org/cmocean/); applicable to other fields of science as well)

### Pandas and Matplotlib
There are some features from Matplotlib that interact with Pandas.

**Example:** For some dataframe `df` with columns `y-data` and `x-data`,
```python
x, y = 'x-data', 'y-data'
plt.scatter(x=x, y=y, data=df) # df is imported and the columns given by x and y are used.
```

## Seaborn
An extension to Matplotlib is Seaborn (`seaborn`) that makes common task into defined functions.

```python
import seaborn as sns
```

**Example: ** Taking a data from dataframe `df` we wish to graph by `x-data` and `y-data` using column `color-data` as the color indicator
```python
sns.lmplot(x=x, y=y, data=df, hue='color-data')
```

## Plotly
Interactive plotting rendered either server-based (`plotly`) or locally (`ploty.offline`).

```python
import plotly as py
import plotly.offline as py
```