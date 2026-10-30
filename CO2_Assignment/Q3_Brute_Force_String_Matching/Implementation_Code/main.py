"""Q3: Brute-force pattern matching with character comparison counts."""
import time

def brute_force_match(text, pattern):
    comparisons = 0
    start = time.perf_counter()
    if pattern == "":
        return 0, comparisons, time.perf_counter()-start
    for shift in range(len(text)-len(pattern)+1):
        j = 0
        while j < len(pattern):
            comparisons += 1
            if text[shift+j] != pattern[j]:
                break
            j += 1
        if j == len(pattern):
            return shift, comparisons, time.perf_counter()-start
    return -1, comparisons, time.perf_counter()-start

def main():
    tests = [
        ("Quick early match", "ALERT: disk full; routine logs follow", "ALERT"),
        ("Repeated-prefix worst-style miss", "A"*30 + "B", "A"*10 + "C"),
        ("Late match", "x"*25 + "SIGNATURE" + "y"*10, "SIGNATURE"),
    ]
    print("Q3 BRUTE-FORCE STRING MATCHING")
    for label, text, pattern in tests:
        idx, comps, elapsed = brute_force_match(text, pattern)
        print(f"{label}: text_len={len(text)} pattern={pattern!r} result_index={idx} char_comparisons={comps} time={elapsed:.8f}s")
if __name__ == "__main__": main()
