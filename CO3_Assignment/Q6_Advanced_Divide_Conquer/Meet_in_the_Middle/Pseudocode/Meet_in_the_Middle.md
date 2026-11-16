# Meet-in-the-Middle Subset Sum
```text
MITM-SUBSET-SUM(A,target)
    split A into L and R
    generate all subset sums SL of L
    generate all subset sums SR of R
    sort SR
    for each x in SL
        binary search for target-x in SR
        if found: return TRUE
    return FALSE
```
