"""Corrected reference implementation of the SentinelOps SOC module."""
import math

def sort_alerts(alerts):
    """Stable insertion sort by severity descending; preserves equal-severity order."""
    for i in range(1, len(alerts)):
        key = alerts[i]
        j = i - 1
        while j >= 0 and alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1
        alerts[j + 1] = key
    return alerts

def is_blocked(blocklist, ip):
    """Return True iff ip occurs in the supplied blocklist."""
    for address in blocklist:
        if address == ip:
            return True
    return False

def find_signature(log, pattern):
    """Return every (including overlapping) starting index of pattern in log."""
    n, m = len(log), len(pattern)
    if m == 0:
        return list(range(n + 1))
    hits = []
    for i in range(n - m + 1):
        j = 0
        while j < m and log[i + j] == pattern[j]:
            j += 1
        if j == m:
            hits.append(i)
    return hits

def closest_logins(events):
    """Return closest event-index pair and Euclidean distance; None if <2 events."""
    if len(events) < 2:
        return None, None
    best_pair = None
    best_d2 = float("inf")
    for i in range(len(events) - 1):
        for j in range(i + 1, len(events)):
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]
            d2 = dx * dx + dy * dy
            if d2 < best_d2:
                best_d2 = d2
                best_pair = (i, j)
    return best_pair, math.sqrt(best_d2)

if __name__ == "__main__":
    alerts = [("A1", 3), ("A2", 9), ("A3", 5), ("A4", 9), ("A5", 1)]
    blocklist = ["10.0.0.5", "10.0.0.9", "172.16.4.2"]
    queries = ["10.0.0.9", "10.0.0.5", "8.8.8.8"]
    log, pattern = "FAILFAIXFAIL", "FAIL"
    events = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print("alerts:", sort_alerts(alerts.copy()))
    print("blocked:", [(ip, is_blocked(blocklist, ip)) for ip in queries])
    print("signature hits:", find_signature(log, pattern))
    print("closest logins:", closest_logins(events))
