**Tips**
1. show mathplot graph 

   The same statements are the data preparation
    ```
    df = pd.DataFrame({ 'means' : results})
    df.plot(title="Law of Large Numbers")
    plt.xlabel("Number of throws in sample")
    plt.ylabel("Average Of Sample")
    ```  
   Display in **cpython** 
    ```
    plt.show()
    ```
   Display in **ipython**
    ```
    %matplotlib inline
    ```