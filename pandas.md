1. DataFrame.plot()
```
DataFrame.plot(x=None, y=None, kind='line', ax=None, subplots=False, sharex=None, sharey=False, layout=None, figsize=None, use_index=True, title=None, grid=None, legend=True, style=None, logx=False, logy=False, loglog=False, xticks=None, yticks=None, xlim=None, ylim=None, rot=None, fontsize=None, colormap=None, table=False, yerr=None, xerr=None, secondary_y=False, sort_columns=False, **kwds)
```
Parameters:

- data : DataFrame
- x : label or position, default None
- y : label or position, default None
- kind : str
     - ‘line’ : line plot (default)
     - ‘bar’ : vertical bar plot
     - ‘barh’ : horizontal bar plot
     - ‘hist’ : histogram
     - ‘box’ : boxplot
     - ‘kde’ : Kernel Density Estimation plot
     - ‘density’ : same as ‘kde’
     - ‘area’ : area plot
     - ‘pie’ : pie plot
     - ‘scatter’ : scatter plot
     - ‘hexbin’ : hexbin plot
- ax : matplotlib axes object, default None
- subplots : boolean, default False.Make separate subplots for each column
- sharex : boolean, default True if ax is None else False
In case subplots=True, share x axis and set some x axis labels to invisible; defaults to True if ax is None otherwise False if an ax is passed in; Be aware, that passing in both an ax and sharex=True will alter all x axis labels for all axis in a figure!
- sharey : boolean, default False.In case subplots=True, share y axis and set some y axis labels to invisible
- layout : tuple (optional),(rows, columns) for the layout of subplots
- figsize : a tuple (width, height) in inches
- title : string or list
- grid : boolean, default None (matlab style default)

Returns:	

- axes : matplotlib.AxesSubplot or np.array of them


2. DataFrame.hist()
``` 
DataFrame.hist(data, column=None, by=None, grid=True, xlabelsize=None, xrot=None, ylabelsize=None, yrot=None, ax=None, sharex=False, sharey=False, figsize=None, layout=None, bins=10, **kwds)[source]
```

Parameter:

- data : DataFrame
- column : string or sequence,If passed, will be used to limit data to a subset of columns
- by : object, optional,If passed, then used to form histograms for separate groups
- grid : boolean, default True,Whether to show axis grid lines
- xlabelsize : int, default None,If specified changes the x-axis label size
- xrot : float, default None
- rotation of x axis labels
- ylabelsize : int, default None,If specified changes the y-axis label size
- yrot : float, default None
- rotation of y axis labels
- ax : matplotlib axes object, default None
- sharex : boolean, default True if ax is None else False,In case subplots=True, share x axis and set some x axis labels to invisible; defaults to True if ax is None otherwise False if an ax is - passed in; Be aware, that passing in both an ax and sharex=True will alter all x axis labels for all subplots in a figure!
- sharey : boolean, default False,In case subplots=True, share y axis and set some y axis labels to invisible
- figsize : tuple, The size of the figure to create in inches by default
- layout : tuple, optional,Tuple of (rows, columns) for the layout of the histograms
- bins : integer, default 10
- Number of histogram bins to be used
- kwds : other plotting keyword arguments,To be passed to hist function
