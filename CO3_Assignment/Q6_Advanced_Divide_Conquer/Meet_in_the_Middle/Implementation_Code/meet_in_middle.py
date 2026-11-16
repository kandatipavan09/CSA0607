"""Q6B: Meet-in-the-Middle subset sum."""
from bisect import bisect_left
def subset_sums(values):
    sums=[0]
    for x in values:
        sums += [s+x for s in sums]
    return sums
def meet_in_middle(values,target):
    mid=len(values)//2
    left=subset_sums(values[:mid])
    right=sorted(subset_sums(values[mid:]))
    for s in left:
        need=target-s
        i=bisect_left(right,need)
        if i<len(right) and right[i]==need:
            return True,s,need,len(left),len(right)
    return False,None,None,len(left),len(right)
def brute_subset_sum(values,target):
    sums={0}
    for x in values: sums |= {s+x for s in list(sums)}
    return target in sums
def main():
    vals=[3,7,2,9,4,1,8,5]; target=17
    found,a,b,nl,nr=meet_in_middle(vals,target)
    print("Q6B - MEET-IN-THE-MIDDLE SUBSET SUM")
    print("Values:",vals,"Target:",target)
    print("Found:",found,"Witness half sums:",a,b)
    print("Left subset sums:",nl,"Right subset sums:",nr)
    print("Brute-force cross-check:",brute_subset_sum(vals,target))
    print("Time and memory: O(2^(n/2)) subset sums per half; memory O(2^(n/2)).")
if __name__=="__main__": main()
