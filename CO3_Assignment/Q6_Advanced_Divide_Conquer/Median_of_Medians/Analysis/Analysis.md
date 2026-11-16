# Median of Medians Analysis

Groups of five produce a pivot whose rank is sufficiently central to guarantee that a constant fraction of elements can be discarded. A standard bound is T(n) ≤ T(n/5) + T(7n/10) + O(n), which solves to O(n). The guarantee prevents repeatedly disastrous partitions in the worst case. QuickSelect has expected O(n) time with randomized pivots but worst-case O(n²). Pivot quality controls how much data is discarded per partition.
