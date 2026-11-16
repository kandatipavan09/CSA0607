"""Q2: Merge Sort and Quick Sort (last-element pivot, comparison/depth instrumentation)."""
def merge_sort(a):
    if len(a) <= 1:
        return a[:]
    mid = len(a)//2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]

def quick_sort(a):
    stats = {"comparisons": 0, "max_depth": 0, "partitions": []}
    def sort(lo, hi, depth):
        stats["max_depth"] = max(stats["max_depth"], depth)
        if lo >= hi: return
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            stats["comparisons"] += 1
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]; i += 1
        a[i], a[hi] = a[hi], a[i]
        stats["partitions"].append((i-lo, hi-i))
        sort(lo, i-1, depth+1)
        sort(i+1, hi, depth+1)
    sort(0, len(a)-1, 1)
    return a, stats

def main():
    sample = [29, 10, 14, 37, 13, 5, 22]
    print("Q2 - MERGE SORT AND QUICK SORT")
    print("Input:", sample)
    print("Merge Sort:", merge_sort(sample))
    result, stats = quick_sort(sample[:])
    print("Quick Sort (last-element pivot):", result)
    print("Quick Sort comparisons:", stats["comparisons"])
    print("Maximum recursion depth:", stats["max_depth"])
    print("Partition sizes (left,right):", stats["partitions"])
    print("Sorted correctly:", result == sorted(sample) == merge_sort(sample))

if __name__ == "__main__":
    main()
