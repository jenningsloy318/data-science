1. show mathplot graph 

   The same statements are the data preparation
    ```
    df = pd.DataFrame({ 'means' : results})
    df.plot(title="Law of Large Numbers")
    plt.xlabel("Number of throws in sample")
    plt.ylabel("Average Of Sample")
    plt.grid(True)
    plt.title("some title")
    ```  
    or
    ```
    plt.plot(list1,list2)  // list1 -->x axis, list2 -->y axis
    plt.title("Law of Large Numbers")
    plt.xlabel("Number of throws in sample")
    plt.ylabel("Average Of Sample")
    plt.grid(True)
    plt.title("some title")
    ```
    or
    ```
    fig,ax=plt.subplots()
    ax.plot(x, y)
    ax.set_title("some title")
    ax.set_xlabel("xlabel")
    ax.set_ylabel("ylabel")
    fig.suptitle("Overall title")
    fig.show()
    ``` 
    - subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
    - Axes(fig, rect, facecolor=None, frameon=True, sharex=None, sharey=None, label=u'', xscale=None, yscale=None, axisbg=None, **kwargs, details [Axes](https://matplotlib.org/devdocs/api/axes_api.html#matplotlib.axes.Axes)
    - Figure(figsize=None, dpi=None, facecolor=None, edgecolor=None, linewidth=0.0, frameon=None, subplotpars=None, tight_layout=None), details [Figure](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure)
   
   Display in **cpython** 
    ```
    plt.show()
    ```
   Display in **ipython**
    ```
    %matplotlib inline
    ```

    ##for multiple plot, we need to  layout setting
    
    - subplot2grid
    ```
    fig = plt.figure(figsize=(8, 6))

    ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
    ax1.plot(x, y)
    ax1.set_title("some title")
    ax1.set_xlabel("xlabel")
    ax1.set_ylabel("ylabel")
    
    ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=1)
    ...(ax2 setting)

    ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=1)
    ...(ax3 setting)

    fig.suptitle("Analysis of Friends")
    fig.tight_layout()
    ```

    - subplots_adjust

    ```
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
        - left  = 0.125  # the left side of the subplots of the figure
        - right = 0.9    # the right side of the subplots of the figure
        - bottom = 0.1   # the bottom of the subplots of the figure
        - top = 0.9      # the top of the subplots of the figure
        - wspace = 0.2   # the amount of width reserved for blank space between subplots
        - hspace = 0.2   # the amount of height reserved for white space between subplots
    ```