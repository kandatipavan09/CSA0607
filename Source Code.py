"""CSA06 CO1_AT1 - ShopSphere scalability audit.
Compact output version: prints results only, not long derivations.
"""

import math

N = 1_000_000
OPS_PER_SECOND = 10
LIMIT_SECONDS = 600


def m1_count(n):
    return n * (n - 1) // 2


def m2_count(n):
    if n <= 1:
        return 0
    return 2 ** ((n - 1).bit_length()) - 1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons


def runtime(operations):
    seconds = operations / OPS_PER_SECOND
    if seconds < 60:
        return f"{seconds:.2f} sec"
    if seconds < 3600:
        return f"{seconds / 60:.2f} min"
    if seconds < 86400:
        return f"{seconds / 3600:.2f} hr"
    return f"{seconds / 86400:.2f} days"


def status(operations):
    return "PASS" if operations / OPS_PER_SECOND <= LIMIT_SECONDS else "FAIL"


def main():
    print("SHOPSPHERE SCALABILITY AUDIT")
    print("-" * 42)

    # M1
    print("\nM1 - Duplicate detector")
    print(f"Sample comparisons (n=4): {m1_count(4)}")
    print(f"Comparisons (n={N:,}): {m1_count(N):,}")
    print(f"Estimated time: {runtime(m1_count(N))} | 10-min target: {status(m1_count(N))}")

    # M2
    print("\nM2 - API rate limiter")
    print(f"Audits (n=1,024): {m2_count(1024):,}")
    print(f"Audits (n={N:,}): {m2_count(N):,}")
    print(f"Estimated time: {runtime(m2_count(N))} | 10-min target: {status(m2_count(N))}")

    # M3 S2
    print("\nM3 - Binary search (S2)")
    sample = list(range(1, 17))
    index, comparisons = binary_search(sample, 11)
    print(f"Sample target: 11 | index: {index} | comparisons: {comparisons}")
    print(f"Estimated comparisons at n={N:,}: {math.ceil(math.log2(N))}")

    # M4 reference estimates
    print("\nM4 - Recommendation engine")
    current = N ** 2
    proposed = N * math.log2(N)
    print(f"Current design (n^2 proxy): {current:,.0f} ops | {runtime(current)} | {status(current)}")
    print(f"Proposed design (n log2 n proxy): {proposed:,.0f} ops | {runtime(proposed)} | {status(proposed)}")

    # M5 reference estimate
    print("\nM5 - Sales analytics")
    m5 = N * (math.log2(N) ** 2)
    print(f"n(log2 n)^2 proxy: {m5:,.0f} ops")
    print(f"Estimated time: {runtime(m5)} | 10-min target: {status(m5)}")

    print("\nFINAL DECISION")
    print("Redesign: M1 and M4")
    print("M2 is linear but exceeds the time limit at 10 ops/sec.")
    print("Keep S2; benchmark M5 with real implementation data.")
    print("\nNote: M4/M5 operation counts are asymptotic proxies, not exact counts.")


if __name__ == "__main__":
    main()
