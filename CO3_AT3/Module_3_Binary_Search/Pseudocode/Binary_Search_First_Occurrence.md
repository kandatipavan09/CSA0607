# Binary Search – First Occurrence

```text
FIRST-OCCURRENCE(A, target)
    low = 0
    high = length(A)          // half-open interval
    while low < high
        mid = floor((low + high) / 2)
        if A[mid].timestamp < target
            low = mid + 1
        else
            high = mid
    if low < length(A) and A[low].timestamp = target
        return low
    return NOT-FOUND
```

This is a lower-bound search. It continues into the left half after finding an equal value, so the returned index is the first occurrence.
