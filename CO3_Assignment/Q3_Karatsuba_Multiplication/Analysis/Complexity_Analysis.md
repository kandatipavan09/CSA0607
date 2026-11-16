# Q3 Analysis

Let n be the number of digits and split each operand into two halves. Karatsuba computes z2 = ac, z0 = bd, and z1 = (a+b)(c+d)-z2-z0. Thus only three half-size recursive multiplications are needed.

**Recurrence:** T(n) = 3T(n/2) + Θ(n). By the Master Theorem, T(n) = Θ(n^(log₂3)) ≈ Θ(n^1.585), compared with Θ(n²) for grade-school digit multiplication.

Asymptotic superiority does not guarantee a win for small operands: recursion, allocations, additions, conversion and interpreter overhead can dominate. The practical crossover depends on implementation and hardware. Measure repeated runs at increasing digit lengths; do not claim a universal crossover value.
