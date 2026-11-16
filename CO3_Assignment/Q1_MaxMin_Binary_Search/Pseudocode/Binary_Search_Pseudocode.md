# Binary Search

```text
BINARY-SEARCH(A, target)
    low = 0; high = length(A) - 1
    while low <= high
        mid = floor((low + high) / 2)
        if A[mid] = target: return mid
        if target < A[mid]: high = mid - 1
        else: low = mid + 1
    return NOT-FOUND
```

Precondition: A is sorted. Each decision discards half of the remaining interval.
