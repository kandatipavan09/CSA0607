# Q2 Analysis

**Merge Sort:** T(n) = 2T(n/2) + Θ(n), giving Θ(n log n) in best, average and worst cases. Its split is by index and is consistently balanced. Auxiliary storage is Θ(n).

**Quick Sort:** With partition cost Θ(n), T(n) = T(k) + T(n-k-1) + Θ(n). Balanced partitions give Θ(n log n); repeated 0:(n-1) partitions give Θ(n²). Recursion stack is Θ(log n) when balanced and Θ(n) in the worst case. This implementation uses the last element as pivot, making already sorted data a poor case.

**Design decision:** For unknown input distributions, consider stability, memory limits, worst-case guarantees, expected input order, pivot strategy, data size and implementation/library guarantees. Randomized or introspective Quick Sort variants can reduce risk; Merge Sort offers predictable time and stability at extra memory cost.
