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