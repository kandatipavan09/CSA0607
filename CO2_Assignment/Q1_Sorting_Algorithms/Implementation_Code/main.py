"""Q1: Compare Selection, Bubble, and Insertion Sort with operation counts."""
import time

def selection_sort(values):
    a = values.copy(); comparisons = swaps = movements = 0
    start = time.perf_counter()
    for i in range(len(a)-1):
        min_i = i
        for j in range(i+1, len(a)):
            comparisons += 1
            if a[j] < a[min_i]: min_i = j
        if min_i != i:
            a[i], a[min_i] = a[min_i], a[i]
            swaps += 1
    return a, comparisons, swaps, movements, time.perf_counter()-start

def bubble_sort(values):
    a = values.copy(); comparisons = swaps = movements = 0
    start = time.perf_counter()
    for end in range(len(a)-1, 0, -1):
        changed = False
        for j in range(end):
            comparisons += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1; changed = True
        if not changed: break
    return a, comparisons, swaps, movements, time.perf_counter()-start

def insertion_sort(values):
    a = values.copy(); comparisons = shifts = 0
    start = time.perf_counter()
    for i in range(1, len(a)):
        key = a[i]; j = i-1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j+1] = a[j]; shifts += 1; j -= 1
            else: break
        a[j+1] = key
    return a, comparisons, 0, shifts, time.perf_counter()-start

def main():
    tests = {
        "Nearly sorted": [10, 20, 30, 25, 40, 50, 45, 60],
        "Reverse order": [80, 70, 60, 50, 40, 30, 20, 10],
        "Edge case (duplicates/negative)": [3, -1, 3, 0, -1, 2, 2, 0],
    }
    algorithms = [("Selection", selection_sort), ("Bubble", bubble_sort), ("Insertion", insertion_sort)]
    print("Q1 SORTING EXPERIMENTS")
    for label, data in tests.items():
        print(f"\n{label}: input={data}")
        for name, fn in algorithms:
            result, comps, swaps, shifts, elapsed = fn(data)
            print(f"{name:10} sorted={result} comparisons={comps} swaps={swaps} shifts/movements={shifts} time={elapsed:.8f}s")
if __name__ == "__main__": main()
