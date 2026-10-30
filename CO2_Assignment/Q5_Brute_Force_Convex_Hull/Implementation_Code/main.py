"""Q5: Brute-force convex hull using the all-points-on-one-side principle."""
import time

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull_bruteforce(points):
    pts = list(dict.fromkeys(points))
    n = len(pts); edge_candidates = 0; side_tests = 0; edges = set()
    start = time.perf_counter()
    if n < 3: return pts, 0, 0, time.perf_counter()-start
    for i in range(n):
        for j in range(i+1, n):
            edge_candidates += 1
            has_left = has_right = False
            for k in range(n):
                if k == i or k == j: continue
                side_tests += 1
                val = cross(pts[i], pts[j], pts[k])
                if val > 0: has_left = True
                elif val < 0: has_right = True
                if has_left and has_right: break
            if not (has_left and has_right):
                edges.add((pts[i], pts[j]))
    # Collect hull vertices, then order around centroid for readable boundary output.
    vertices = sorted({p for edge in edges for p in edge})
    if vertices:
        cx = sum(p[0] for p in vertices)/len(vertices); cy = sum(p[1] for p in vertices)/len(vertices)
        vertices.sort(key=lambda p: __import__("math").atan2(p[1]-cy, p[0]-cx))
    return vertices, edge_candidates, side_tests, time.perf_counter()-start

def main():
    tests = {
        "Boundary plus interior": [(0,0),(4,0),(4,4),(0,4),(2,2),(1,2),(3,1)],
        "Challenge: collinear points and duplicates": [(0,0),(2,0),(4,0),(4,3),(2,1),(0,3),(0,0),(1,1)],
    }
    print("Q5 BRUTE-FORCE CONVEX HULL")
    for label, points in tests.items():
        hull, candidates, tests_count, elapsed = convex_hull_bruteforce(points)
        print(f"{label}: unique_points={len(set(points))} hull_vertices={hull}")
        print(f"edge_candidates={candidates} side_tests={tests_count} time={elapsed:.8f}s")
if __name__ == "__main__": main()
