"""KartIQ Module 3: Binary search for first matching timestamp."""
def first_timestamp(orders, target):
    """orders is sorted ascending by timestamp; returns first matching index or -1."""
    lo, hi = 0, len(orders)
    comparisons=0
    # lower_bound: first index whose timestamp is >= target
    while lo < hi:
        mid=(lo+hi)//2
        comparisons += 1
        if orders[mid][0] < target:
            lo=mid+1
        else:
            hi=mid
    if lo < len(orders):
        comparisons += 1
        if orders[lo][0] == target:
            return lo, comparisons
    return -1, comparisons

def main():
    orders=[(101,"O4"),(102,"O2"),(102,"O5"),(103,"O6"),(105,"O1"),(105,"O3")]
    print("KARTIQ MODULE 3 - FIRST-OCCURRENCE BINARY SEARCH")
    print("Consolidated orders:",orders)
    for target in [102,105,104]:
        idx,count=first_timestamp(orders,target)
        print(f"timestamp={target}: index={idx}, order={orders[idx] if idx!=-1 else 'NOT FOUND'}, comparisons={count}")
    print("Maximum ordinary binary-search comparisons for 10,000,000 entries: 24")
    print("First-occurrence lower-bound search: at most 24 midpoint comparisons plus one final equality check.")

if __name__=="__main__":
    main()
