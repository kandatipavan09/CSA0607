"""Q1: Divide-and-conquer maximum/minimum and iterative binary search."""
def max_min(a):
    """Returns (minimum, maximum, comparison_count) using divide and conquer."""
    if not a:
        raise ValueError("Input must not be empty")
    def solve(lo, hi):
        if lo == hi:
            return a[lo], a[lo], 0
        if hi == lo + 1:
            return (a[lo], a[hi], 1) if a[lo] <= a[hi] else (a[hi], a[lo], 1)
        mid = (lo + hi) // 2
        mn1, mx1, c1 = solve(lo, mid)
        mn2, mx2, c2 = solve(mid + 1, hi)
        mn = mn1 if mn1 < mn2 else mn2
        mx = mx1 if mx1 > mx2 else mx2
        return mn, mx, c1 + c2 + 2
    return solve(0, len(a) - 1)

def binary_search(a, target):
    """Returns (index or -1, comparison_count); input must be sorted."""
    lo, hi, count = 0, len(a) - 1, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        count += 1
        if a[mid] == target:
            return mid, count
        count += 1
        if target < a[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1, count

def main():
    data = [18, 4, 27, 9, 2, 31, 14, 6]
    mn, mx, comparisons = max_min(data)
    ordered = sorted(data)
    found, c_found = binary_search(ordered, 14)
    missing, c_missing = binary_search(ordered, 15)
    print("Q1 - MAXIMUM AND MINIMUM")
    print("Input:", data)
    print(f"Minimum={mn}, Maximum={mx}, comparisons={comparisons}")
    print("\nQ1 - BINARY SEARCH")
    print("Sorted input:", ordered)
    print(f"Search 14 -> index {found}, comparisons={c_found}")
    print(f"Search 15 -> index {missing}, comparisons={c_missing}")
    print("All checks:", mn == min(data) and mx == max(data) and ordered[found] == 14 and missing == -1)

if __name__ == "__main__":
    main()
