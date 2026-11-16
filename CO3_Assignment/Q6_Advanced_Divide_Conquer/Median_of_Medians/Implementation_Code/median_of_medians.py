"""Q6A: Median of Medians selection and randomized QuickSelect baseline."""
import random
def median_of_medians_select(a, k):
    """Return 0-based k-th smallest item; deterministic worst-case O(n)."""
    if not 0 <= k < len(a): raise ValueError("k out of range")
    if len(a) <= 5: return sorted(a)[k]
    groups=[a[i:i+5] for i in range(0,len(a),5)]
    medians=[sorted(g)[len(g)//2] for g in groups]
    pivot=median_of_medians_select(medians,len(medians)//2)
    lows=[x for x in a if x<pivot]
    highs=[x for x in a if x>pivot]
    equals=[x for x in a if x==pivot]
    if k<len(lows): return median_of_medians_select(lows,k)
    if k<len(lows)+len(equals): return pivot
    return median_of_medians_select(highs,k-len(lows)-len(equals))
def quickselect(a,k):
    if not 0<=k<len(a): raise ValueError("k out of range")
    a=a[:]
    while True:
        if len(a)==1:return a[0]
        pivot=random.choice(a)
        lows=[x for x in a if x<pivot]; highs=[x for x in a if x>pivot]
        eq=[x for x in a if x==pivot]
        if k<len(lows): a=lows
        elif k<len(lows)+len(eq): return pivot
        else: k-=len(lows)+len(eq); a=highs
def main():
    data=[29,10,14,37,13,5,22,18,4,31,6,25,11]
    k=5
    m=median_of_medians_select(data,k); q=quickselect(data,k)
    print("Q6A - MEDIAN OF MEDIANS")
    print("Input:",data); print(f"k={k+1} (1-based)")
    print("Median of Medians result:",m)
    print("QuickSelect result:",q)
    print("Sorted reference:",sorted(data)[k])
    print("Both correct:",m==q==sorted(data)[k])
    print("Median of Medians worst-case time: O(n); QuickSelect expected O(n), worst-case O(n^2).")
if __name__=="__main__": main()
