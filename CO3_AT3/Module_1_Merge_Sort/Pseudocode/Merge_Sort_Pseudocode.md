# Stable Merge Sort – Pseudocode

```text
MERGE-SORT(A)
    if length(A) <= 1
        return A
    mid = floor(length(A) / 2)
    L = MERGE-SORT(A[0 : mid])
    R = MERGE-SORT(A[mid : n])
    return STABLE-MERGE(L, R)

STABLE-MERGE(L, R)
    result = empty list
    while L and R are not empty
        if L.first.timestamp <= R.first.timestamp
            append L.first to result
            remove L.first from L
        else
            append R.first to result
            remove R.first from R
    append remaining elements of L and R
    return result
```

The `<=` comparison is essential: when timestamps are equal, the item from the left run (earlier in the original sequence) is selected first, preserving stability.
