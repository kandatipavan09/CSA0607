"""Q4: Conventional and Strassen matrix multiplication for square matrices."""
def add(A, B):
    n=len(A); return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]
def sub(A, B):
    n=len(A); return [[A[i][j]-B[i][j] for j in range(n)] for i in range(n)]
def conventional(A, B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def split(M):
    n=len(M); m=n//2
    return ([row[:m] for row in M[:m]], [row[m:] for row in M[:m]],
            [row[:m] for row in M[m:]], [row[m:] for row in M[m:]])
def join(C11,C12,C21,C22):
    top=[C11[i]+C12[i] for i in range(len(C11))]
    bot=[C21[i]+C22[i] for i in range(len(C21))]
    return top+bot
def strassen(A, B, cutoff=1):
    n=len(A)
    if n <= cutoff: return conventional(A,B)
    if n%2: raise ValueError("Strassen recursive input size must be even; pad first.")
    a,b,c,d=split(A); e,f,g,h=split(B)
    p1=strassen(a, sub(f,h), cutoff)
    p2=strassen(add(a,b), h, cutoff)
    p3=strassen(add(c,d), e, cutoff)
    p4=strassen(d, sub(g,e), cutoff)
    p5=strassen(add(a,d), add(e,h), cutoff)
    p6=strassen(sub(b,d), add(g,h), cutoff)
    p7=strassen(sub(a,c), add(e,f), cutoff)
    c11=add(sub(add(p5,p4),p2),p6)
    c12=add(p1,p2)
    c21=add(p3,p4)
    c22=sub(sub(add(p1,p5),p3),p7)
    return join(c11,c12,c21,c22)
def pad(M, size):
    n=len(M); return [row+[0]*(size-n) for row in M]+[[0]*size for _ in range(size-n)]
def unpad(M,n): return [row[:n] for row in M[:n]]
def strassen_any(A,B):
    n=len(A); size=1
    while size<n: size*=2
    return unpad(strassen(pad(A,size),pad(B,size)),n)
def main():
    A=[[1,2,3],[4,5,6],[7,8,9]]
    B=[[9,8,7],[6,5,4],[3,2,1]]
    c=conventional(A,B); s=strassen_any(A,B)
    print("Q4 - STRASSEN MATRIX MULTIPLICATION")
    print("Matrix A:", A); print("Matrix B:", B)
    print("Conventional result:", c)
    print("Strassen result:", s)
    print("Non-power-of-two padding used: 3x3 -> 4x4")
    print("Results match:", c == s)
    print("Complexities: Conventional O(n^3); Strassen O(n^log2(7)) ~= O(n^2.807).")
if __name__ == "__main__": main()
