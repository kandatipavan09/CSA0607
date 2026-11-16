# Module 1 – Nightly Order Consolidation

## Requirement and design
Sort all orders by timestamp for the audit report. Stability is mandatory: orders sharing a timestamp must retain their original arrival order. Stable Merge Sort is selected because it guarantees O(n log n) time and predictable decomposition.

## Divide, conquer and combine
- Divide: split the six-order list into two halves recursively.
- Conquer: sort each half.
- Combine: merge the two sorted runs. On equal timestamps, choose from the left run first.

## Complete trace
Input:
`[(105,O1),(102,O2),(105,O3),(101,O4),(102,O5),(103,O6)]`

Splits:
- `[(105,O1),(102,O2),(105,O3)]` and `[(101,O4),(102,O5),(103,O6)]`
- Left side: `[(105,O1)]` + `[(102,O2),(105,O3)]`
- Right side: `[(101,O4)]` + `[(102,O5),(103,O6)]`
- Sort left pair: `[(102,O2),(105,O3)]`; merge with `(105,O1)` → `[(102,O2),(105,O1),(105,O3)]`
- Sort right pair: `[(102,O5),(103,O6)]`; merge with `(101,O4)` → `[(101,O4),(102,O5),(103,O6)]`
- Final merge:
  1. 101 O4
  2. 102 O2 (tie: left run selected)
  3. 102 O5
  4. 103 O6
  5. 105 O1 (tie: left run selected)
  6. 105 O3

Final stable output:
`[(101,O4),(102,O2),(102,O5),(103,O6),(105,O1),(105,O3)]`

## Recurrence and solution
For n greater than one:
`T(n) = 2T(n/2) + Θ(n)`, with `T(1)=Θ(1)`.
At each recursion level, merging processes n records; there are log₂n levels. Thus `T(n)=Θ(n log₂n)`.

For n=10,000,000:
- `log₂(n) ≈ 23.2535`
- `n log₂(n) ≈ 232,534,966` as the leading n log n work estimate.
- A balanced-tree comparison estimate is about `n log₂n − n + 1 ≈ 222,534,967` comparisons; actual comparisons depend on input order and merge-run lengths. A conservative worst-case bound for arbitrary n can be given by `n⌈log₂n⌉ − 2^⌈log₂n⌉ + 1`, which is approximately 233 million for this n.

## Memory and production handling
In-memory Merge Sort needs Θ(n) auxiliary records in addition to the input, plus Θ(log n) recursion stack. If all 10 million records do not fit in RAM, use external Merge Sort: create sorted chunks that fit in memory, write each run to disk, then perform a k-way merge using a min-heap and buffered sequential I/O. This trades disk I/O and temporary storage for bounded RAM.

## Trade-off
Stable order and predictable O(n log n) performance require O(n) extra memory. If RAM is constrained, external sorting adds I/O and operational complexity.
