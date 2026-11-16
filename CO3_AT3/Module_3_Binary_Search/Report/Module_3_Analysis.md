# Module 3 – Order Lookup

## Requirement
Support staff search for an order timestamp in the consolidated list and need the first order when several entries share a timestamp. Binary Search requires the Module 1 output to be sorted by timestamp.

## Recurrence
Each comparison discards approximately half the remaining interval:
`T(n)=T(n/2)+Θ(1)`.
After k steps, remaining size is n/2^k. Set this to 1:
`n/2^k ≤ 1`, so `k ≥ log₂n`; therefore time is Θ(log n), and iterative extra space is Θ(1).

For 10,000,000 orders:
`log₂(10,000,000) ≈ 23.2535`, so ordinary binary search requires at most `⌊log₂n⌋+1 = 24` midpoint comparisons.
The first-occurrence implementation uses lower-bound search: at most 24 midpoint comparisons, followed by at most one equality check (25 timestamp comparisons under this counting convention).

## First occurrence
Use a lower-bound variant. When `A[mid].timestamp >= target`, move `high` left to `mid`; otherwise move `low` to `mid+1`. After convergence, verify equality. This guarantees the earliest matching timestamp.

## Trade-off
Lookup is fast, but sorted order must be maintained. If the data is not sorted, Binary Search is invalid; sort first or use a suitable index/hash-based design depending on query requirements.
