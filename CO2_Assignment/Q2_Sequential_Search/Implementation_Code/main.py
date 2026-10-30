"""Q2: Sequential search experiments across positions, misses, and list sizes."""
import time

def sequential_search(records, target):
    comparisons = 0
    start = time.perf_counter()
    for index, record in enumerate(records):
        comparisons += 1
        if record["tool_id"] == target:
            return index, comparisons, time.perf_counter()-start
    return -1, comparisons, time.perf_counter()-start

def make_records(n):
    return [{"tool_id": f"T-{i:04d}", "technician_id": f"TECH-{i%17:02d}",
             "issue_time": f"09:{i%60:02d}", "work_bay": f"BAY-{i%8+1}"} for i in range(n)]

def main():
    print("Q2 SEQUENTIAL SEARCH")
    for n in (10, 100, 1000, 5000):
        records = make_records(n)
        cases = [("first", records[0]["tool_id"]), ("middle", records[n//2]["tool_id"]),
                 ("last", records[-1]["tool_id"]), ("unsuccessful", "T-MISSING")]
        for label, target in cases:
            idx, comps, elapsed = sequential_search(records, target)
            print(f"n={n:4d} case={label:12s} index={idx:5d} comparisons={comps:5d} time={elapsed:.8f}s")
if __name__ == "__main__": main()
