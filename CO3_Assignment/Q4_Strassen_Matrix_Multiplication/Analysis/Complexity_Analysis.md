# Q4 Analysis

Conventional block multiplication performs eight half-size matrix multiplications: T(n)=8T(n/2)+Θ(n²)=Θ(n³). Strassen replaces these with seven products and extra matrix additions/subtractions: T(n)=7T(n/2)+Θ(n²)=Θ(n^(log₂7))≈Θ(n^2.807).

The implementation pads a non-power-of-two square matrix with zeros to the next power of two and removes padding after multiplication. Padding increases work and memory. For small matrices, additions, temporary matrices, recursion and cache effects can make conventional multiplication faster. The supplied 3×3 test checks correctness, not a universal speed crossover.
