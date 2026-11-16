"""Q3: Standard and Karatsuba integer multiplication."""
def standard_multiply(x, y):
    return x * y

def karatsuba(x, y, threshold=1):
    if x < 0 or y < 0:
        sign = -1 if (x < 0) ^ (y < 0) else 1
        return sign * karatsuba(abs(x), abs(y), threshold)
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    base = 10 ** m
    high1, low1 = divmod(x, base)
    high2, low2 = divmod(y, base)
    z0 = karatsuba(low1, low2, threshold)
    z2 = karatsuba(high1, high2, threshold)
    z1 = karatsuba(low1 + high1, low2 + high2, threshold) - z0 - z2
    return z2 * base * base + z1 * base + z0

def main():
    x = 12345678901234567890
    y = 98765432109876543210
    s, k = standard_multiply(x, y), karatsuba(x, y)
    print("Q3 - KARATSUBA MULTIPLICATION")
    print("X:", x); print("Y:", y)
    print("Standard product:", s)
    print("Karatsuba product:", k)
    print("Products match:", s == k)
    print("Complexities: Standard digit multiplication O(n^2); Karatsuba O(n^log2(3)) ~= O(n^1.585).")

if __name__ == "__main__":
    main()
