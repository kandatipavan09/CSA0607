# Divide-and-Conquer Closest Pair
```text
CLOSEST(Px, Py)
    if |P| <= 3: solve by checking all pairs
    split points by x-coordinate into L and R
    partition Py into Ly and Ry while preserving y order
    (dL,pL) = CLOSEST(Lx,Ly)
    (dR,pR) = CLOSEST(Rx,Ry)
    d = min(dL,dR); best pair = corresponding pair
    build strip of points within distance d of dividing line
    scan strip in y-order; compare only following points whose y-gap < d
    update best pair and return
```
