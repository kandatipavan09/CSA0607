# KartIQ – Case Understanding and Final Design

## (a) Understand the case

| Module | Requirement | Key issue | Poor algorithm consequence | Selected design |
|---|---|---|---|---|
| 1 Nightly order consolidation | Sort 10 million orders by timestamp | Stability, RAM capacity, predictable runtime | Audit order of equal timestamps can be corrupted; slow sort misses deadline | Stable Merge Sort; external merge if RAM is insufficient |
| 2 Live seller leaderboard | Re-sort 100,000 seller scores repeatedly | Nearly sorted data; first-pivot worst case | Extreme partitions can cause O(n²) work and sale-event freezes | Median-of-three Quick Sort with introspective fallback; benchmark adaptive stable sort |
| 3 Order lookup | Find first order at timestamp | Input must be sorted; duplicates require first match | Linear scan is slow; ordinary binary search may return any duplicate | Lower-bound Binary Search |
| 4 Recommendation scores | Multiply 1,024×1,024 matrices | Multiplication count, memory, additions, cache, padding | Conventional O(n³) may be costly; naive Strassen use can lose in practice | Hybrid blocked conventional/Strassen with tuned cutoff |

## (f) Final platform design

| Module | Algorithm | Time | Extra memory | Main reason | Trade-off | Change condition |
|---|---|---|---|---|---|---|
| 1 | Stable Merge Sort | O(n log n) | O(n) | Stable and predictable | Needs auxiliary memory | If data exceeds RAM, external merge sort |
| 2 | Median-of-three Quick Sort + introsort fallback | O(n log n) worst-case with fallback | O(log n) typical stack; O(n) theoretical stack before fallback | Reduces predictable bad pivots and bounds worst case | More logic and pivot/fallback overhead | If near-sorted updates dominate, use adaptive Timsort or incremental ordered index |
| 3 | Lower-bound Binary Search | O(log n) | O(1) | Finds first duplicate in sorted data | Requires sorted data | If frequent unsorted writes dominate, maintain an index or use a different lookup structure |
| 4 | Hybrid Strassen/blocked conventional | O(n^log₂7) above cutoff asymptotically; conventional O(n³) below cutoff | O(n²) temporary storage in straightforward implementations | Reduces recursive scalar multiplications for sufficiently large matrices | Additions, memory and numerical effects | If matrices are small/sparse or memory-limited, use conventional blocked/sparse multiplication |

## Production workload calculations
- Merge Sort for 10,000,000 records: log₂n≈23.2535; leading n log₂n≈232.5 million; balanced comparison estimate about 222.5 million.
- First-pivot Quick Sort worst-case for 100,000 ordered sellers: n(n−1)/2=4,999,950,000 comparisons.
- Binary Search for 10,000,000 orders: ordinary maximum 24 midpoint comparisons; lower-bound variant up to 24 midpoint comparisons plus final equality check.
- Matrix n=1,024: conventional 1,073,741,824 scalar multiplications; Strassen 282,475,249.

## Final recommendation
Use stable Merge Sort for audit correctness, guarded Quick Sort for leaderboard responsiveness, lower-bound Binary Search for duplicate timestamps, and a measured hybrid matrix multiplication strategy. Monitor wall-clock latency, memory pressure, stability and error tolerance in production.
