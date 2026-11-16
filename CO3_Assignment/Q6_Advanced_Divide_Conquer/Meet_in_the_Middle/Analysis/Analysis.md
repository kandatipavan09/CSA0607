# Meet-in-the-Middle Analysis

For n values, split into two halves. Each half has about 2^(n/2) subset sums. Sorting one list and binary-searching complements gives approximately O(n·2^(n/2)) time including sorting/searching in this simple implementation, and O(2^(n/2)) memory. Straight enumeration explores O(2^n) subsets. The technique trades extra storage for a smaller search space and is useful when n is moderate and memory is available.
