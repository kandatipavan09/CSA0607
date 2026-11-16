# Karatsuba Pseudocode
```text
KARATSUBA(x, y)
    if x or y is a single digit: return x*y
    split x = a*B + b and y = c*B + d
    z0 = KARATSUBA(b,d)
    z2 = KARATSUBA(a,c)
    z1 = KARATSUBA(a+b,c+d) - z0 - z2
    return z2*B^2 + z1*B + z0
```
Only three recursive multiplications are required.
