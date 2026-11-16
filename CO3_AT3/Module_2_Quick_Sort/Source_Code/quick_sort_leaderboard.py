"""KartIQ Module 2: Quick Sort with median-of-three pivot and instrumentation."""
def median_of_three(a, lo, hi):
    mid = (lo + hi) // 2
    trio = [(a[lo],lo),(a[mid],mid),(a[hi],hi)]
    trio.sort(key=lambda item:item[0])
    return trio[1][1]

def quick_sort(a):
    stats={"comparisons":0,"partitions":[]}
    def sort(lo,hi):
        if lo >= hi: return
        pivot_idx=median_of_three(a,lo,hi)
        a[pivot_idx],a[hi]=a[hi],a[pivot_idx]
        pivot=a[hi]
        i=lo
        for j in range(lo,hi):
            stats["comparisons"] += 1
            if a[j] <= pivot:
                a[i],a[j]=a[j],a[i]
                i+=1
        a[i],a[hi]=a[hi],a[i]
        stats["partitions"].append({"pivot":pivot,"left":i-lo,"right":hi-i})
        sort(lo,i-1)
        sort(i+1,hi)
    sort(0,len(a)-1)
    return a,stats

def first_pivot_partition(values):
    """One Lomuto-style partition using first element as pivot."""
    a=values[:]
    pivot=a[0]
    rest=[x for x in a[1:] if x<=pivot]
    greater=[x for x in a[1:] if x>pivot]
    return rest+[pivot]+greater, pivot, len(rest), len(greater)

def main():
    scores=[42,17,63,8,55,29]
    traced,pivot,left,right=first_pivot_partition(scores)
    print("KARTIQ MODULE 2 - QUICK SORT")
    print("Sample scores:",scores)
    print(f"First-pivot partition trace: pivot={pivot}, left={left}, right={right}, result={traced}")
    improved,stats=quick_sort(scores[:])
    print("Improved median-of-three result:",improved)
    print("Partition records:",stats["partitions"])
    print("Partition comparisons:",stats["comparisons"])
    print("Sorted correctly:",improved==sorted(scores))
    print("Production recommendation: median-of-three or randomized pivot; use introsort depth fallback for worst-case protection.")

if __name__=="__main__":
    main()
