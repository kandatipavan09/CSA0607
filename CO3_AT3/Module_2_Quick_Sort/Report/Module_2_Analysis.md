# Module 2 – Live Seller Leaderboard

## Requirement and problem
Sort 100,000 seller scores every few seconds. Scores change only slightly between refreshes, so the data is nearly sorted. The existing first-element pivot can repeatedly select an extreme pivot on sorted or nearly sorted input, producing highly unbalanced partitions and long freezes.

## Sample first-pivot partition trace
Input: `[42,17,63,8,55,29]`
- Pivot = first element = 42.
- Values ≤ 42: `[17,8,29]` (3 values).
- Values > 42: `[63,55]` (2 values).
- Partition result: `[17,8,29,42,63,55]`.
This demonstrates one partition; recursive calls then sort the two sides.

## Recurrences
Best/balanced split:
`T(n)=2T(n/2)+cn = Θ(n log n)`.
Worst/extreme split:
`T(n)=T(n−1)+cn = Θ(n²)`.
For the worst case, comparisons are `n(n−1)/2`.

For 100,000 sellers:
`100,000 × 99,999 / 2 = 4,999,950,000` comparisons in the worst case.
A balanced comparison scale is approximately `n log₂n ≈ 1,660,964` (leading-order estimate; exact count depends on partition implementation).

## Improved strategy
Use median-of-three (first, middle, last) or randomized pivoting to make predictable extreme splits less likely. For stronger worst-case protection, use Introsort: begin with Quick Sort, monitor recursion depth, and switch to Heap Sort when depth exceeds `2⌊log₂n⌋`. Since scores are nearly sorted, also benchmark an adaptive stable algorithm such as Timsort for real production use; it can exploit existing runs. The assignment's required Quick Sort module is still implemented with median-of-three pivot.

## Trade-offs
Median-of-three adds a small pivot-selection cost and does not mathematically eliminate all bad cases. Randomization adds randomness and makes runs less reproducible. Introsort adds implementation complexity but provides O(n log n) worst-case protection. If stability is required, use a stable sort.
