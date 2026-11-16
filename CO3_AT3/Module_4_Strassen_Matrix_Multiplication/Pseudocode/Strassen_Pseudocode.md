# Strassen's Matrix Multiplication – Pseudocode

For A = [[A11,A12],[A21,A22]] and B = [[B11,B12],[B21,B22]], compute:

```text
M1 = (A11 + A22)(B11 + B22)
M2 = (A21 + A22)B11
M3 = A11(B12 - B22)
M4 = A22(B21 - B11)
M5 = (A11 + A12)B22
M6 = (A21 - A11)(B11 + B12)
M7 = (A12 - A22)(B21 + B22)

C11 = M1 + M4 - M5 + M7
C12 = M3 + M5
C21 = M2 + M4
C22 = M1 - M2 + M3 + M6
```

Recursively multiply the seven products and combine the four C blocks. Use conventional multiplication below a chosen cutoff. Pad non-power-of-two dimensions with zeros and trim the result.
