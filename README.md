# intern-at-the-Institute-of-Basic-Science

------
## Summary

Strategy in the education means a sequence that contains learning material with some info. ex)Expected learning time, How important it is(weight).
We wanna get the strategy with E-learning data.
The data was so dirty that we make them fancy by using Pandas.
After that, We apply scheduling algorithm for getting optimal stategy.

We made the datas to tree structure by referring student's curriculum and applied the expanded c-mu rule to the tree.

Expanded c-mu rule is c-mu rule in the tree.(original c-mu rule was defined just in the set of sequences.)
We easily proved the Expanded c-mu rule and applied it.(And some people proved this earlier except for we.)

The code for Expanded c-mu rule is in the **'scheduling'** folder.

And in the Gittin index folder and Baum welch folder, there are out trial and errors.
For not hierarchical structure, we can use gittin index and baum-welch algorithm but they are not useful for hierarchical structure.
------
