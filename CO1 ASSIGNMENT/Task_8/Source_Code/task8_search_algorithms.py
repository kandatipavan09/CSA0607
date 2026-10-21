"""
CSA06 - Design and Analysis of Algorithms
Task 8: Implementation and Testing

Algorithms:
1. Iterative Linear Search
2. Recursive Binary Search
3. Hash Table Search (Python dictionary)

Input sizes: 1,000; 10,000; 100,000; 1,000,000 records.

Run:
    python task8_search_algorithms.py

The program records elapsed time for each algorithm and writes:
    task8_results.csv

Notes:
- Each registration number is represented by an integer.
- Binary search is tested on sorted records.
- Hash-table construction is timed separately from lookup.
- Lookup timing uses a target at the end of the list to make linear
  search exercise its worst case and to provide a repeatable comparison.
- Timings depend on hardware, operating system, and Python version.
"""

import csv
import time

SIZES = [1_000, 10_000, 100_000, 1_000_000]


def linear_search(records, target):
    """Return the index of target, or -1 if it is not present."""
    for i, value in enumerate(records):
        if value == target:
            return i
    return -1


def recursive_binary_search(records, left, right, target):
    """Search a sorted list recursively; return index or -1."""
    if left > right:
        return -1

    mid = (left + right) // 2

    if records[mid] == target:
        return mid
    if target < records[mid]:
        return recursive_binary_search(records, left, mid - 1, target)
    return recursive_binary_search(records, mid + 1, right, target)


def timed_call(function, *args):
    start = time.perf_counter()
    result = function(*args)
    elapsed = time.perf_counter() - start
    return result, elapsed


def main():
    output_path = "task8_results.csv"
    rows = []

    print("TASK 8: SEARCH ALGORITHM IMPLEMENTATION AND TESTING")
    print("-" * 78)
    print(f"{'Records':>12} | {'Linear (s)':>12} | {'Binary (s)':>12} | "
          f"{'Hash build (s)':>14} | {'Hash lookup (s)':>15}")
    print("-" * 78)

    for n in SIZES:
        # Unique, sorted student registration numbers.
        records = list(range(1, n + 1))
        target = n  # Present at the end: worst case for linear search.

        linear_result, linear_time = timed_call(linear_search, records, target)
        binary_result, binary_time = timed_call(
            recursive_binary_search, records, 0, len(records) - 1, target
        )

        hash_table, hash_build_time = timed_call(
            lambda: {registration: index
                     for index, registration in enumerate(records)}
        )
        hash_result, hash_lookup_time = timed_call(
            hash_table.get, target, -1
        )

        # Validate correctness before saving results.
        expected_index = n - 1
        if not (
            linear_result == expected_index
            and binary_result == expected_index
            and hash_result == expected_index
        ):
            raise AssertionError(f"Incorrect result for input size {n}")

        row = {
            "records": n,
            "target": target,
            "linear_result_index": linear_result,
            "linear_time_seconds": f"{linear_time:.9f}",
            "binary_result_index": binary_result,
            "binary_time_seconds": f"{binary_time:.9f}",
            "hash_build_time_seconds": f"{hash_build_time:.9f}",
            "hash_result_index": hash_result,
            "hash_lookup_time_seconds": f"{hash_lookup_time:.9f}",
        }
        rows.append(row)

        print(f"{n:>12,} | {linear_time:>12.9f} | {binary_time:>12.9f} | "
              f"{hash_build_time:>14.9f} | {hash_lookup_time:>15.9f}")

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("-" * 78)
    print("All algorithms returned the correct registration record.")
    print(f"Results saved to: {output_path}")
    print("Use the measured times in Task 9; do not copy example timings.")


if __name__ == "__main__":
    main()
