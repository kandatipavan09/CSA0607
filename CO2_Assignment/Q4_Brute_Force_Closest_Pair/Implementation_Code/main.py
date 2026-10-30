"""Q4: Brute-force closest pair in 2D; counts unique pairs and distance calculations."""
import math, random, time

def closest_pair(points):
    if len(points) < 2: raise ValueError("At least two points are required")
    best_pair = None; best_d2 = float("inf"); pairs = distances = 0
    start = time.perf_counter()
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            pairs += 1; distances += 1
            dx = points[i][0]-points[j][0]; dy = points[i][1]-points[j][1]
            d2 = dx*dx + dy*dy
            if d2 < best_d2:
                best_d2 = d2; best_pair = (points[i], points[j])
    elapsed = time.perf_counter()-start
    return best_pair, math.sqrt(best_d2), pairs, distances, elapsed

def main():
    random.seed(17)
    print("Q4 BRUTE-FORCE CLOSEST PAIR")
    for n in (20, 100, 500, 1000):
        points = [(random.randrange(0, 100000), random.randrange(0, 100000)) for _ in range(n)]
        pair, distance, pairs, calculations, elapsed = closest_pair(points)
        expected = n*(n-1)//2
        print(f"n={n:4d} pairs={pairs:8d} expected={expected:8d} distance_calculations={calculations:8d} min_distance={distance:.3f} time={elapsed:.6f}s pair={pair}")
if __name__ == "__main__": main()
