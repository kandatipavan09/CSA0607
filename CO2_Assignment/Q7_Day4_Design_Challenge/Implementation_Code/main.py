"""Q7: Diagnose sequential search and redesign repeated lookups with a hash index."""
import time, random

def sequential_search(records, target):
    comparisons = 0
    for record in records:
        comparisons += 1
        if record["tool_id"] == target: return record, comparisons
    return None, comparisons

def indexed_search(index, target):
    # One dictionary lookup after O(n) preprocessing.
    return index.get(target), 1

def main():
    print("Q7 DAY-4 DESIGN CHALLENGE: SEQUENTIAL SEARCH -> HASH INDEX")
    print("Prediction: after O(n) index construction, repeated lookups should average O(1) rather than O(n).")
    for n in (100, 1000, 5000, 20000):
        records = [{"tool_id": f"T-{i:06d}", "technician_id": f"TECH-{i%31:02d}",
                    "issue_time": "10:30", "work_bay": f"BAY-{i%12+1}"} for i in range(n)]
        targets = [records[-1]["tool_id"]] * 100
        t0 = time.perf_counter()
        index = {r["tool_id"]: r for r in records}
        build_time = time.perf_counter()-t0
        seq_ops = idx_ops = 0
        t0 = time.perf_counter()
        for target in targets:
            _, c = sequential_search(records, target); seq_ops += c
        seq_time = time.perf_counter()-t0
        t0 = time.perf_counter()
        for target in targets:
            indexed_search(index, target); idx_ops += 1
        hash_time = time.perf_counter()-t0
        print(f"n={n:5d} lookups={len(targets):3d} sequential_comparisons={seq_ops:8d} indexed_lookups={idx_ops:4d} index_build={build_time:.6f}s sequential={seq_time:.6f}s indexed={hash_time:.6f}s")
    print("Trade-off: additional O(n) memory and index maintenance on issue/return; original search remains simple for tiny or one-off lists.")
if __name__ == "__main__": main()
