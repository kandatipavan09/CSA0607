# Quick Sort – Pseudocode

```text
QUICK-SORT(A, low, high)
    if low < high
        pivotIndex = MEDIAN-OF-THREE(A[low], A[mid], A[high])
        move pivot to end
        p = PARTITION(A, low, high)
        QUICK-SORT(A, low, p - 1)
        QUICK-SORT(A, p + 1, high)
```

For production, use a depth-limited introspective variant: if recursion depth exceeds a multiple of log₂n, switch to Heap Sort. This protects worst-case O(n log n) time. Randomized pivoting is another way to avoid predictable adversarial input.
