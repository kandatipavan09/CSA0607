# Q5 Analysis

Brute force checks n(n−1)/2 pairs and takes Θ(n²) time. Divide-and-conquer sorts points initially, recursively solves left and right halves, and checks a narrow strip around the dividing line. With y-order preserved and geometric packing limiting relevant neighbors, the recurrence is T(n)=2T(n/2)+Θ(n)=Θ(n log n).

The strip does not compare every point with every other point: only points whose x-distance from the dividing line is less than the current best distance are included, and y-order permits stopping once the y-gap is at least the best distance. The included implementation reports actual distance calculations on its sample; use larger identical datasets to demonstrate growth experimentally.
