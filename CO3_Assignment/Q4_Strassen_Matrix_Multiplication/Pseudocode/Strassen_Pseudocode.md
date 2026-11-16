# Strassen Pseudocode
```text
STRASSEN(A,B)
    if matrix is small: return conventional_multiply(A,B)
    partition A into A11,A12,A21,A22 and B into B11,B12,B21,B22
    compute seven products:
      M1=(A11+A22)(B11+B22)
      M2=(A21+A22)B11
      M3=A11(B12-B22)
      M4=A22(B21-B11)
      M5=(A11+A12)B22
      M6=(A21-A11)(B11+B12)
      M7=(A12-A22)(B21+B22)
    reconstruct four result blocks from M1...M7
    return combined matrix
```
