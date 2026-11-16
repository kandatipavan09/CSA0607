# Merge Sort Pseudocode
```text
MERGE-SORT(A)
    if length(A) <= 1: return A
    split A into L and R
    L = MERGE-SORT(L)
    R = MERGE-SORT(R)
    return MERGE(L, R) by repeatedly taking the smaller front element
```
