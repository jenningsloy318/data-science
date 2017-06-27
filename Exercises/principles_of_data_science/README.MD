**Tips**
code repo: 

https://github.com/PacktPublishing/Principles-of-Data-Science
1. show mathplot graph 

   The same statements are the data preparation
    ```
    df = pd.DataFrame({ 'means' : results})
    df.plot(title="Law of Large Numbers")
    plt.xlabel("Number of throws in sample")
    plt.ylabel("Average Of Sample")
    ```  
    or
    ```
    plt.plot(list1,list2)  // list1 -->x axis, list2 -->y axis
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