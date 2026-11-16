# Divide-and-Conquer Maximum and Minimum

```text
MAXMIN(A, low, high)
    if low = high
        return (A[low], A[low])
    if high = low + 1
        compare A[low] and A[high]
        return (smaller, larger)
    mid = floor((low + high) / 2)
    (minL, maxL) = MAXMIN(A, low, mid)
    (minR, maxR) = MAXMIN(A, mid + 1, high)
    return (min(minL, minR), max(maxL, maxR))
```

Each recursive call returns the minimum and maximum of its segment. The combine step uses two comparisons.
