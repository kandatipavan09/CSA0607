"""Optimised SentinelOps module for production-style repeated lookups."""
import math

def sort_alerts(alerts):
    """Stable insertion sort, suitable for small/nearly sorted batches."""
    for i in range(1, len(alerts)):
        key = alerts[i]
        j = i - 1
        while j >= 0 and alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1
        alerts[j + 1] = key
    return alerts

def make_blocklist_index(blocklist):
    """Build a set for expected O(1) average membership queries."""
    return set(blocklist)

def is_blocked(blocklist_or_set, ip):
    """Membership check; pass a set for repeated production queries."""
    return ip in blocklist_or_set

def find_signature(log, pattern):
    """Find all occurrences using a linear-time KMP scan, including overlaps."""
    if pattern == "":
        return list(range(len(log) + 1))
    # Build the longest-prefix-suffix table.
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    hits = []
    i = j = 0
    while i < len(log):
        if log[i] == pattern[j]:
            i += 1; j += 1
            if j == len(pattern):
                hits.append(i - j)
                j = lps[j - 1]
        elif j:
            j = lps[j - 1]
        else:
            i += 1
    return hits

def closest_logins(events):
    """Exact brute-force closest pair using unique pairs and squared distances.
    For 8,000 points, O(n^2) remains costly. Exact branch-and-bound is not safe
    without spatial indexing; this implementation keeps exact output and counts
    no square roots inside the pair loop.
    """
    if len(events) < 2:
        return None, None, 0
    best_pair = None
    best_d2 = float("inf")
    distance_computations = 0
    for i in range(len(events) - 1):
        xi, yi = events[i]
        for j in range(i + 1, len(events)):
            dx = xi - events[j][0]
            dy = yi - events[j][1]
            d2 = dx * dx + dy * dy
            distance_computations += 1
            if d2 < best_d2:
                best_d2 = d2
                best_pair = (i, j)
    return best_pair, math.sqrt(best_d2), distance_computations

def closest_logins_bruteforce_count(events):
    """Baseline brute-force counter, for benchmark comparison."""
    n = len(events)
    if n < 2: return None, None, 0
    best_pair = None; best_d2 = float("inf"); count = 0
    for i in range(n):
        for j in range(n):
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]
            d2 = dx*dx + dy*dy
            count += 1
            d = math.sqrt(d2)
            if d > 0 and (best_pair is None or d < best_d2):
                best_d2 = d; best_pair = (i, j)
    return best_pair, math.sqrt(best_d2) if best_pair else 0, count

def run_tests():
    """Deterministic unit tests including required boundary conditions."""
    assert sort_alerts([("A1",3),("A2",9),("A3",5),("A4",9),("A5",1)]) == [
        ("A2",9),("A4",9),("A3",5),("A1",3),("A5",1)]
    assert sort_alerts([]) == []
    assert sort_alerts([("X",4),("Y",4)]) == [("X",4),("Y",4)]
    block = ["10.0.0.5","10.0.0.9","172.16.4.2"]
    assert is_blocked(make_blocklist_index(block), "10.0.0.9") is True
    assert is_blocked(make_blocklist_index(block), "8.8.8.8") is False
    assert is_blocked(make_blocklist_index([]), "8.8.8.8") is False
    assert find_signature("FAILFAIXFAIL","FAIL") == [0,8]
    assert find_signature("abcXYZ","XYZ") == [3]
    assert find_signature("abc","longer") == []
    assert find_signature("aaaa","aa") == [0,1,2]
    assert find_signature("abc","") == [0,1,2,3]
    assert closest_logins([]) == (None,None,0)
    assert closest_logins([(1,2)]) == (None,None,0)
    pair, dist, count = closest_logins([(0,0),(3,4),(1,1)])
    assert pair == (0,2) and abs(dist-math.sqrt(2)) < 1e-12
    print("ALL OPTIMISED MODULE TESTS PASSED")

if __name__ == "__main__":
    run_tests()
    alerts = [("A1", 3), ("A2", 9), ("A3", 5), ("A4", 9), ("A5", 1)]
    blocklist = ["10.0.0.5", "10.0.0.9", "172.16.4.2"]
    print("sorted:", sort_alerts(alerts))
    index = make_blocklist_index(blocklist)
    print("blocked:", [(ip, is_blocked(index, ip)) for ip in ["10.0.0.9","10.0.0.5","8.8.8.8"]])
    print("signature hits:", find_signature("FAILFAIXFAIL", "FAIL"))
    print("closest:", closest_logins([(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]))
