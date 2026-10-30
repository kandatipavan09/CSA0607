"""Q6: Exhaustive 0-1 knapsack for humanitarian airlift package selection."""
import time

def exhaustive_knapsack(packages, capacity):
    n = len(packages); candidates = 0; feasible = 0
    best_value = 0; best_weight = 0; best_ids = []
    start = time.perf_counter()
    for mask in range(1 << n):
        candidates += 1; weight = value = 0; chosen = []
        for i, (pid, w, v) in enumerate(packages):
            if mask & (1 << i):
                weight += w; value += v; chosen.append(pid)
        if weight <= capacity:
            feasible += 1
            if value > best_value:
                best_value, best_weight, best_ids = value, weight, chosen
    return best_ids, best_weight, best_value, candidates, feasible, time.perf_counter()-start

def main():
    small = [("P1", 2, 6), ("P2", 2, 10), ("P3", 3, 12), ("P4", 1, 4)]
    print("Q6 EXHAUSTIVE SEARCH")
    print("Correctness instance: capacity=5, packages=(ID,weight,value)", small)
    result = exhaustive_knapsack(small, 5)
    print(f"best_ids={result[0]} weight={result[1]} value={result[2]} candidates={result[3]} feasible={result[4]} time={result[5]:.8f}s")
    for n in (8, 12, 16, 20):
        packages = [(f"P{i+1}", (i*7)%9+1, (i*11)%20+5) for i in range(n)]
        result = exhaustive_knapsack(packages, max(10, n*2))
        print(f"n={n:2d} candidates={result[3]:8d} theoretical={2**n:8d} feasible={result[4]:8d} best_value={result[2]:4d} time={result[5]:.6f}s")
if __name__ == "__main__": main()
