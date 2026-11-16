"""KartIQ Module 4: Strassen matrix multiplication (square matrices, zero padding)."""
def add(A,B):
    n=len(A); return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]
def sub(A,B):
    n=len(A); return [[A[i][j]-B[i][j] for j in range(n)] for i in range(n)]
def conventional(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def split(M):
    n=len(M); m=n//2
    return ([r[:m] for r in M[:m]],[r[m:] for r in M[:m]],
            [r[:m] for r in M[m:]],[r[m:] for r in M[m:]])
def join(a,b,c,d):
    return [a[i]+b[i] for i in range(len(a))]+[c[i]+d[i] for i in range(len(c))]
def strassen(A,B,cutoff=1):
    n=len(A)
    if n<=cutoff: return conventional(A,B)
    a,b,c,d=split(A); e,f,g,h=split(B)
    p1=strassen(a,sub(f,h),cutoff)
    p2=strassen(add(a,b),h,cutoff)
    p3=strassen(add(c,d),e,cutoff)
    p4=strassen(d,sub(g,e),cutoff)
    p5=strassen(add(a,d),add(e,h),cutoff)
    p6=strassen(sub(b,d),add(g,h),cutoff)
    p7=strassen(sub(a,c),add(e,f),cutoff)
    c11=add(sub(add(p5,p4),p2),p6)
    c12=add(p1,p2)
    c21=add(p3,p4)
    c22=sub(sub(add(p1,p5),p3),p7)
    return join(c11,c12,c21,c22)
def pad(M,size):
    n=len(M)
    return [r+[0]*(size-n) for r in M]+[[0]*size for _ in range(size-n)]
def trim(M,n):
    return [r[:n] for r in M[:n]]
def strassen_any(A,B,cutoff=1):
    n=len(A); size=1
    while size<n: size*=2
    return trim(strassen(pad(A,size),pad(B,size),cutoff),n)
def main():
    A=[[1,7],[3,5]]
    B=[[1,3],[7,5]]
    print("KARTIQ MODULE 4 - STRASSEN MATRIX MULTIPLICATION")
    print("A =",A); print("B =",B)
    print("Conventional C =",conventional(A,B))
    print("Strassen C =",strassen_any(A,B))
    print("Verified:",conventional(A,B)==strassen_any(A,B))
    n=1024
    print(f"n={n}: conventional scalar multiplications = {n**3:,}")
    print(f"n={n}: Strassen scalar multiplications = {7**10:,} (7^log2(1024))")
    print("Hybrid recommendation: conventional multiplication below a tuned cutoff; Strassen above it.")

if __name__=="__main__":
    main()
