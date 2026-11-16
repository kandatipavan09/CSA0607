# Median of Medians
```text
SELECT(A,k)
    if |A| <= 5: sort and return element k
    divide A into groups of at most five
    find each group's median
    pivot = SELECT(medians, middle index)
    partition A into values < pivot, = pivot, > pivot
    recurse only into the partition containing rank k
```
