# Module 4 – Recommendation Scores with Strassen

## Seven products and reconstruction
For 2×2 block matrices:
- M1=(A11+A22)(B11+B22)
- M2=(A21+A22)B11
- M3=A11(B12−B22)
- M4=A22(B21−B11)
- M5=(A11+A12)B22
- M6=(A21−A11)(B11+B12)
- M7=(A12−A22)(B21+B22)

Reconstruct:
- C11=M1+M4−M5+M7
- C12=M3+M5
- C21=M2+M4
- C22=M1−M2+M3+M6

## Verification on sample
A=[[1,7],[3,5]], B=[[1,3],[7,5]].
Conventional product:
C11=1×1+7×7=50; C12=1×3+7×5=38;
C21=3×1+5×7=38; C22=3×3+5×5=34.
So C=[[50,38],[38,34]]. Strassen produces the same matrix.

## Recurrence and scalar multiplications
Conventional: `T(n)=8T(n/2)+Θ(n²)=Θ(n³)`.
Strassen: `T(n)=7T(n/2)+Θ(n²)=Θ(n^log₂7)≈Θ(n^2.807)`.

For n=1,024=2^10:
- Conventional scalar multiplications: n³ = 1,073,741,824.
- Strassen scalar multiplications: 7^10 = 282,475,249.
- Reduction: about 73.7% fewer scalar multiplications (not necessarily 73.7% faster).

## Why may Strassen not be faster?
Strassen introduces many matrix additions/subtractions, temporary matrices, memory allocation, recursion overhead and potentially worse cache behaviour. Numerical stability and rounding error can also matter for floating-point workloads. Padding non-power-of-two sizes adds work.

## Practical hybrid
Use conventional blocked matrix multiplication below an empirically tuned cutoff (for example, a benchmarked block-size threshold), and Strassen only above it. Tune cutoff on production hardware and data type. Reuse buffers, use cache-aware blocks and avoid unnecessary allocations. At n=1,024, benchmark both implementations rather than assuming the asymptotic count guarantees lower wall-clock time.
