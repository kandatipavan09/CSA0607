# Q1 Analysis

**Max-Min recurrence:** T(n) = 2T(n/2) + 2 for n greater than 2, with constant-size base cases. Therefore T(n) = O(n). For n a power of two, the tournament-style algorithm uses approximately 3n/2 - 2 comparisons (the implementation handles odd segments recursively; count is returned by the program). Two independent scans use 2n - 2 comparisons.

**Binary Search:** T(n) = T(n/2) + O(1), so worst-case time is O(log n); iterative auxiliary space is O(1). It requires sorted input.

**Interpretation:** Max-Min reduces comparisons by allowing each half to summarize its extrema. Binary Search eliminates a half of the remaining sorted range after each comparison decision.
