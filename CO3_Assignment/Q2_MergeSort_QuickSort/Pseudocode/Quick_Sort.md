# Quick Sort Pseudocode (last element as pivot)
```text
QUICK-SORT(A, low, high)
    if low < high
        p = PARTITION(A, low, high)
        QUICK-SORT(A, low, p-1)
        QUICK-SORT(A, p+1, high)
```
Partition moves values <= pivot to its left and larger values to its right.
